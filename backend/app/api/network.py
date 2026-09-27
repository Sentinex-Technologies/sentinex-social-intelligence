"""
Network Analysis API endpoints - Component E: Link Analysis & Network Topology.
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.services.network_analysis import NetworkAnalyzer

router = APIRouter()


@router.get("/build")
async def build_network_graph(
    platform: Optional[str] = None,
    min_followers: int = 0,
    db: Session = Depends(get_db)
):
    """
    Build the social network graph from database.
    
    **Query Parameters:**
    - platform: Filter by platform (twitter, telegram, instagram, etc.)
    - min_followers: Minimum follower count to include users
    
    Returns basic network statistics after building.
    """
    try:
        analyzer = NetworkAnalyzer(db)
        graph = analyzer.build_network_graph(platform=platform, min_followers=min_followers)
        stats = analyzer.get_network_statistics()
        
        return {
            "status": "success",
            "message": "Network graph built successfully",
            "statistics": stats
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Graph building failed: {str(e)}")


@router.get("/statistics")
async def get_network_statistics(
    platform: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Get comprehensive network statistics.
    
    Includes:
    - Number of nodes (users) and edges (relationships)
    - Network density and connectivity
    - Average clustering coefficient
    - Degree distribution
    """
    try:
        analyzer = NetworkAnalyzer(db)
        analyzer.build_network_graph(platform=platform)
        stats = analyzer.get_network_statistics()
        
        return {
            "status": "success",
            "network_statistics": stats
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Statistics computation failed: {str(e)}")


@router.get("/opinion-leaders")
async def get_opinion_leaders(
    top_n: int = Query(default=10, ge=1, le=100),
    metric: str = Query(default="pagerank", regex="^(pagerank|eigenvector|betweenness)$"),
    platform: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Identify top opinion leaders (high-influence users).
    
    **Component E Requirement:** Identify high-influence nodes and opinion leaders.
    
    **Query Parameters:**
    - top_n: Number of top leaders to return (1-100)
    - metric: Centrality metric (pagerank, eigenvector, betweenness)
    - platform: Filter by platform
    
    Opinion leaders are identified using network centrality measures:
    - **PageRank:** Google's algorithm for importance
    - **Eigenvector:** Influence based on influential connections
    - **Betweenness:** Bridge between different communities
    """
    try:
        analyzer = NetworkAnalyzer(db)
        analyzer.build_network_graph(platform=platform)
        leaders = analyzer.identify_opinion_leaders(top_n=top_n, metric=metric)
        
        # Enrich with user details
        from app.models.user import User
        enriched_leaders = []
        for user_id, score in leaders:
            user = db.query(User).filter(User.id == user_id).first()
            if user:
                enriched_leaders.append({
                    "user_id": user_id,
                    "username": user.username,
                    "platform": user.platform,
                    "followers_count": user.followers_count,
                    "influence_score": user.influence_score,
                    f"{metric}_score": score
                })
        
        return {
            "status": "success",
            "metric_used": metric,
            "opinion_leaders": enriched_leaders
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Opinion leader identification failed: {str(e)}")


@router.get("/propagation/{user_id}")
async def analyze_propagation(
    user_id: int,
    max_depth: int = Query(default=3, ge=1, le=5),
    db: Session = Depends(get_db)
):
    """
    Analyze information propagation from a specific user.
    
    **Component E Requirement:** Track information/sentiment propagation paths.
    
    Shows how information could spread through the network from this user,
    including reachable users at each propagation depth (hops).
    
    **Path Parameters:**
    - user_id: Source user ID
    
    **Query Parameters:**
    - max_depth: Maximum propagation depth (1-5 hops)
    """
    try:
        analyzer = NetworkAnalyzer(db)
        analyzer.build_network_graph()
        propagation = analyzer.analyze_information_propagation(
            source_user_id=user_id,
            max_depth=max_depth
        )
        
        if "error" in propagation:
            raise HTTPException(status_code=404, detail=propagation["error"])
        
        return {
            "status": "success",
            "propagation_analysis": propagation
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Propagation analysis failed: {str(e)}")


@router.get("/communities")
async def detect_communities(
    algorithm: str = Query(default="greedy", regex="^(greedy|louvain)$"),
    platform: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """
    Detect communities (clusters) in the social network.
    
    Communities help identify:
    - Echo chambers
    - Polarized groups
    - Shared interest groups
    
    **Query Parameters:**
    - algorithm: Detection algorithm (greedy, louvain)
    - platform: Filter by platform
    """
    try:
        analyzer = NetworkAnalyzer(db)
        analyzer.build_network_graph(platform=platform)
        communities = analyzer.detect_communities(algorithm=algorithm)
        
        # Count community sizes
        from collections import Counter
        community_sizes = Counter(communities.values())
        
        return {
            "status": "success",
            "algorithm_used": algorithm,
            "num_communities": len(community_sizes),
            "community_sizes": dict(community_sizes),
            "user_communities": communities
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Community detection failed: {str(e)}")


@router.post("/update-influence")
async def update_influence_scores(db: Session = Depends(get_db)):
    """
    Compute and update influence scores for all users.
    
    Influence score is a weighted combination of:
    - PageRank (40%)
    - Eigenvector centrality (30%)
    - Normalized follower count (20%)
    - Engagement rate (10%)
    
    This should be run periodically to keep influence scores up-to-date.
    """
    try:
        analyzer = NetworkAnalyzer(db)
        updated_count = analyzer.update_user_influence_scores()
        
        return {
            "status": "success",
            "message": f"Updated influence scores for {updated_count} users"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Influence update failed: {str(e)}")


@router.get("/export")
async def export_graph_visualization(
    platform: Optional[str] = None,
    min_followers: int = 0,
    db: Session = Depends(get_db)
):
    """
    Export network graph in format suitable for D3.js visualization.
    
    Returns nodes and links arrays ready for frontend rendering.
    
    **Query Parameters:**
    - platform: Filter by platform
    - min_followers: Minimum follower count (useful for large networks)
    """
    try:
        analyzer = NetworkAnalyzer(db)
        analyzer.build_network_graph(platform=platform, min_followers=min_followers)
        graph_data = analyzer.export_graph_for_visualization()
        
        return {
            "status": "success",
            "graph": graph_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Graph export failed: {str(e)}")
