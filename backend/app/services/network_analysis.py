"""
Network Analysis Service - Component E: Link Analysis & Network Topology.

Implements NTRO SIH26152 Component E requirements:
- Follower graph construction
- Centrality measures (degree, betweenness, closeness, eigenvector)
- High-influence node identification
- Opinion leader detection
- Information propagation path analysis
- Sentiment flow visualization data

Uses NetworkX for graph algorithms and analysis.
"""

import networkx as nx
from typing import List, Dict, Tuple, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.user import User, UserRelationship
from app.models.social_post import SocialPost
from app.models.engagement import Engagement


class NetworkAnalyzer:
    """
    Analyzes social network topology and influence patterns.
    
    Provides:
    - Network graph construction from database
    - Influence metrics computation
    - Community detection
    - Propagation path analysis
    """
    
    def __init__(self, db: Session):
        """Initialize analyzer with database session."""
        self.db = db
        self.graph = None
    
    def build_network_graph(
        self,
        platform: Optional[str] = None,
        min_followers: int = 0
    ) -> nx.DiGraph:
        """
        Build a directed network graph from user relationships.
        
        Args:
            platform: Filter by platform (None for all)
            min_followers: Minimum follower count to include user
        
        Returns:
            NetworkX directed graph
        """
        # Query users
        query = self.db.query(User).filter(User.followers_count >= min_followers)
        if platform:
            query = query.filter(User.platform == platform)
        users = query.all()
        
        # Create directed graph
        G = nx.DiGraph()
        
        # Add nodes (users) with attributes
        for user in users:
            G.add_node(
                user.id,
                username=user.username,
                platform=user.platform,
                followers=user.followers_count,
                following=user.following_count,
                posts=user.posts_count,
                influence=user.influence_score,
                location=user.location_region,
                age_range=user.age_range
            )
        
        # Query relationships
        relationships = self.db.query(UserRelationship).filter(
            UserRelationship.follower_id.in_([u.id for u in users]),
            UserRelationship.followed_id.in_([u.id for u in users])
        ).all()
        
        # Add edges (follower -> followed relationships)
        for rel in relationships:
            if G.has_node(rel.follower_id) and G.has_node(rel.followed_id):
                G.add_edge(
                    rel.follower_id,
                    rel.followed_id,
                    weight=rel.interaction_score,
                    created_at=rel.created_at
                )
        
        self.graph = G
        return G
    
    def compute_centrality_measures(self) -> Dict[int, Dict[str, float]]:
        """
        Compute various centrality measures for all nodes.
        
        Centrality measures (Component E requirement):
        - Degree centrality: Number of connections
        - Betweenness centrality: Bridge between communities
        - Closeness centrality: Distance to all other nodes
        - Eigenvector centrality: Influence based on influential connections
        - PageRank: Google's algorithm for importance
        
        Returns:
            Dictionary mapping user_id to centrality scores
        """
        if not self.graph:
            raise ValueError("Graph not built. Call build_network_graph() first.")
        
        G = self.graph
        
        # Compute centrality measures
        degree_cent = nx.degree_centrality(G)
        betweenness_cent = nx.betweenness_centrality(G)
        closeness_cent = nx.closeness_centrality(G)
        eigenvector_cent = nx.eigenvector_centrality(G, max_iter=1000)
        pagerank = nx.pagerank(G)
        
        # Combine into single dictionary per node
        centrality_data = {}
        for node in G.nodes():
            centrality_data[node] = {
                "degree_centrality": degree_cent.get(node, 0.0),
                "betweenness_centrality": betweenness_cent.get(node, 0.0),
                "closeness_centrality": closeness_cent.get(node, 0.0),
                "eigenvector_centrality": eigenvector_cent.get(node, 0.0),
                "pagerank": pagerank.get(node, 0.0)
            }
        
        return centrality_data
    
    def identify_opinion_leaders(
        self,
        top_n: int = 10,
        metric: str = "pagerank"
    ) -> List[Tuple[int, float]]:
        """
        Identify top opinion leaders (high-influence nodes).
        
        Opinion leaders are users who:
        - Have high centrality scores
        - Are well-connected to influential users
        - Bridge different communities
        
        Args:
            top_n: Number of top leaders to return
            metric: Centrality metric to use (pagerank, eigenvector, betweenness)
        
        Returns:
            List of (user_id, score) tuples, sorted by score descending
        """
        centrality_data = self.compute_centrality_measures()
        
        # Extract scores for the specified metric
        scores = [(user_id, data[metric]) for user_id, data in centrality_data.items()]
        
        # Sort by score descending
        scores.sort(key=lambda x: x[1], reverse=True)
        
        return scores[:top_n]
    
    def detect_communities(self, algorithm: str = "louvain") -> Dict[int, int]:
        """
        Detect communities (clusters) in the network.
        
        Communities help identify:
        - Echo chambers
        - Polarized groups
        - Shared interest groups
        
        Args:
            algorithm: Community detection algorithm (louvain, greedy)
        
        Returns:
            Dictionary mapping user_id to community_id
        """
        if not self.graph:
            raise ValueError("Graph not built. Call build_network_graph() first.")
        
        # Convert to undirected for community detection
        G_undirected = self.graph.to_undirected()
        
        if algorithm == "louvain":
            # Louvain method (best for large networks)
            try:
                import community as community_louvain
                partition = community_louvain.best_partition(G_undirected)
            except ImportError:
                # Fallback to greedy modularity
                algorithm = "greedy"
        
        if algorithm == "greedy":
            # Greedy modularity communities
            communities = nx.community.greedy_modularity_communities(G_undirected)
            partition = {}
            for idx, community in enumerate(communities):
                for node in community:
                    partition[node] = idx
        
        return partition
    
    def analyze_information_propagation(
        self,
        source_user_id: int,
        max_depth: int = 3
    ) -> Dict[str, any]:
        """
        Analyze how information could propagate from a source user.
        
        Component E requirement: Track sentiment/information spread paths.
        
        Args:
            source_user_id: Starting user ID
            max_depth: Maximum propagation depth (hops)
        
        Returns:
            Dictionary with propagation metrics and reachable nodes
        """
        if not self.graph:
            raise ValueError("Graph not built. Call build_network_graph() first.")
        
        G = self.graph
        
        if source_user_id not in G:
            return {"error": "User not found in graph"}
        
        # BFS to find reachable nodes at each depth
        reachable_by_depth = {}
        visited = {source_user_id}
        current_level = {source_user_id}
        
        for depth in range(1, max_depth + 1):
            next_level = set()
            for node in current_level:
                # Get followers (users who would see this user's content)
                followers = list(G.predecessors(node))
                for follower in followers:
                    if follower not in visited:
                        next_level.add(follower)
                        visited.add(follower)
            
            reachable_by_depth[depth] = list(next_level)
            current_level = next_level
            
            if not current_level:
                break
        
        # Calculate total reach
        total_reach = sum(len(nodes) for nodes in reachable_by_depth.values())
        
        # Get source user's follower count for comparison
        source_followers = G.nodes[source_user_id].get("followers", 0)
        
        return {
            "source_user_id": source_user_id,
            "max_depth": max_depth,
            "reachable_by_depth": reachable_by_depth,
            "total_reach": total_reach,
            "source_followers": source_followers,
            "amplification_factor": total_reach / max(1, source_followers)
        }
    
    def get_network_statistics(self) -> Dict[str, any]:
        """
        Get overall network statistics.
        
        Returns:
            Dictionary with network metrics
        """
        if not self.graph:
            raise ValueError("Graph not built. Call build_network_graph() first.")
        
        G = self.graph
        
        # Basic stats
        num_nodes = G.number_of_nodes()
        num_edges = G.number_of_edges()
        
        # Density (how connected the network is)
        density = nx.density(G)
        
        # Average clustering coefficient
        clustering = nx.average_clustering(G.to_undirected())
        
        # Degree distribution
        degrees = [d for n, d in G.degree()]
        avg_degree = sum(degrees) / len(degrees) if degrees else 0
        max_degree = max(degrees) if degrees else 0
        
        # Connected components
        num_components = nx.number_weakly_connected_components(G)
        largest_component_size = len(max(
            nx.weakly_connected_components(G),
            key=len
        )) if num_nodes > 0 else 0
        
        return {
            "num_users": num_nodes,
            "num_relationships": num_edges,
            "network_density": density,
            "avg_clustering_coefficient": clustering,
            "avg_degree": avg_degree,
            "max_degree": max_degree,
            "num_components": num_components,
            "largest_component_size": largest_component_size,
            "connectivity": largest_component_size / num_nodes if num_nodes > 0 else 0
        }
    
    def update_user_influence_scores(self) -> int:
        """
        Compute and update influence scores for all users in the database.
        
        Influence score is computed as a weighted combination of:
        - PageRank (40%)
        - Eigenvector centrality (30%)
        - Follower count normalized (20%)
        - Engagement rate (10%)
        
        Returns:
            Number of users updated
        """
        if not self.graph:
            self.build_network_graph()
        
        # Compute centrality measures
        centrality_data = self.compute_centrality_measures()
        
        # Get max follower count for normalization
        max_followers = max(
            (self.graph.nodes[n].get("followers", 0) for n in self.graph.nodes()),
            default=1
        )
        
        updated_count = 0
        for user_id, centrality in centrality_data.items():
            user = self.db.query(User).filter(User.id == user_id).first()
            if user:
                # Compute weighted influence score
                normalized_followers = user.followers_count / max_followers
                
                influence_score = (
                    0.40 * centrality["pagerank"] +
                    0.30 * centrality["eigenvector_centrality"] +
                    0.20 * normalized_followers +
                    0.10 * user.avg_engagement_rate
                )
                
                # Update user
                user.influence_score = min(1.0, influence_score)
                user.centrality_score = centrality["betweenness_centrality"]
                user.reach_score = centrality["pagerank"]
                
                updated_count += 1
        
        self.db.commit()
        return updated_count
    
    def export_graph_for_visualization(self) -> Dict[str, List[Dict]]:
        """
        Export graph in format suitable for frontend visualization (D3.js).
        
        Returns:
            Dictionary with 'nodes' and 'links' arrays
        """
        if not self.graph:
            raise ValueError("Graph not built. Call build_network_graph() first.")
        
        G = self.graph
        
        # Compute centrality for node sizing
        pagerank = nx.pagerank(G)
        
        # Export nodes
        nodes = []
        for node_id in G.nodes():
            node_data = G.nodes[node_id]
            nodes.append({
                "id": node_id,
                "username": node_data.get("username", f"user_{node_id}"),
                "platform": node_data.get("platform"),
                "followers": node_data.get("followers", 0),
                "influence": node_data.get("influence", 0),
                "pagerank": pagerank.get(node_id, 0),
                "location": node_data.get("location"),
                "age_range": node_data.get("age_range")
            })
        
        # Export edges
        links = []
        for source, target in G.edges():
            edge_data = G.edges[source, target]
            links.append({
                "source": source,
                "target": target,
                "weight": edge_data.get("weight", 1.0)
            })
        
        return {
            "nodes": nodes,
            "links": links,
            "metadata": self.get_network_statistics()
        }
