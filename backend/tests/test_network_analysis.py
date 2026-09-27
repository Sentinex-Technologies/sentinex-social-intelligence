"""
Tests for network analysis (Component E).
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.services.synthetic_data import SyntheticDataGenerator
from app.services.network_analysis import NetworkAnalyzer


@pytest.fixture
def test_db_with_data():
    """Create a test database with synthetic data."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(bind=engine)
    db = SessionLocal()
    
    # Generate test data
    generator = SyntheticDataGenerator(seed=42)
    generator.generate_complete_dataset(
        db,
        num_users=20,
        num_posts=50,
        days_back=7
    )
    
    yield db
    db.close()


def test_build_network_graph(test_db_with_data):
    """Test network graph construction."""
    analyzer = NetworkAnalyzer(test_db_with_data)
    graph = analyzer.build_network_graph()
    
    assert graph is not None
    assert graph.number_of_nodes() > 0
    assert graph.number_of_edges() > 0


def test_network_statistics(test_db_with_data):
    """Test network statistics computation."""
    analyzer = NetworkAnalyzer(test_db_with_data)
    analyzer.build_network_graph()
    stats = analyzer.get_network_statistics()
    
    assert "num_users" in stats
    assert "num_relationships" in stats
    assert "network_density" in stats
    assert "avg_degree" in stats
    assert stats["num_users"] == 20


def test_community_detection(test_db_with_data):
    """Test community detection."""
    analyzer = NetworkAnalyzer(test_db_with_data)
    analyzer.build_network_graph()
    communities = analyzer.detect_communities(algorithm="greedy")
    
    assert communities is not None
    assert len(communities) > 0
    assert all(isinstance(v, int) for v in communities.values())


def test_propagation_analysis(test_db_with_data):
    """Test information propagation analysis."""
    analyzer = NetworkAnalyzer(test_db_with_data)
    analyzer.build_network_graph()
    
    # Get first user ID
    from app.models.user import User
    user = test_db_with_data.query(User).first()
    
    propagation = analyzer.analyze_information_propagation(
        source_user_id=user.id,
        max_depth=2
    )
    
    assert "total_reach" in propagation
    assert "reachable_by_depth" in propagation
    assert "amplification_factor" in propagation


def test_export_graph_visualization(test_db_with_data):
    """Test graph export for visualization."""
    analyzer = NetworkAnalyzer(test_db_with_data)
    analyzer.build_network_graph()
    export = analyzer.export_graph_for_visualization()
    
    assert "nodes" in export
    assert "links" in export
    assert "metadata" in export
    assert len(export["nodes"]) > 0
    assert len(export["links"]) > 0
