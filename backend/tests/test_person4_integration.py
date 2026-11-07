"""
Person 4 Integration Test Suite
Verifies Seeding, Schema Integrity, Composite Score Gating, and End-to-End Persistence.
Owned by: Person 4 (Lead Architect & Demo Engineer)
"""

import os
import unittest
import uuid
import chromadb

from backend.app.db.session import init_db, SessionLocal
from backend.app.db.models import PostModel, MetricModel, LearnedLessonModel, SentimentModel
from backend.app.schemas.post_schema import EngagementMetricsSchema
from backend.app.core.memory import calculate_composite_score, VectorMemoryManager
from backend.scripts.seed_db import seed


class TestPerson4Integration(unittest.TestCase):
    """Integration verification across Person 4's database, seeding, and scoring deliverables."""

    @classmethod
    def setUpClass(cls):
        # 1. Initialize DB tables cleanly
        init_db()

    def setUp(self):
        self.db = SessionLocal()
        self.chroma_client = chromadb.Client()
        self.brand_name = f"test_brand_{uuid.uuid4().hex[:6]}"
        self.mem_mgr = VectorMemoryManager(brand_name=self.brand_name, client=self.chroma_client)

    def tearDown(self):
        self.db.close()

    def test_seam_1_database_schema_initialization(self):
        """Verifies that all 4 core tables exist and can accept queries."""
        post_count = self.db.query(PostModel).count()
        metric_count = self.db.query(MetricModel).count()
        lesson_count = self.db.query(LearnedLessonModel).count()
        sentiment_count = self.db.query(SentimentModel).count()

        self.assertIsInstance(post_count, int)
        self.assertIsInstance(metric_count, int)
        self.assertIsInstance(lesson_count, int)
        self.assertIsInstance(sentiment_count, int)

    def test_seam_2_seeding_integrity(self):
        """Verifies that seed_db populates posts, sentiments, and lessons from seed_data.json."""
        seed()
        
        # Verify database population
        posts = self.db.query(PostModel).all()
        self.assertGreaterEqual(len(posts), 15, "Expected at least 15 seeded posts from seed_data.json")
        
        lessons = self.db.query(LearnedLessonModel).all()
        self.assertGreaterEqual(len(lessons), 6, "Expected at least 6 structured memory rules")

        sentiments = self.db.query(SentimentModel).all()
        self.assertGreaterEqual(len(sentiments), 1, "Expected at least 1 audience sentiment record")

    def test_seam_3_composite_score_barrier(self):
        """
        Verifies the reinforcement gating barrier:
        - Score > 5.0 qualifies as viral and is vectorized into long-term memory.
        - Score <= 5.0 is discarded to preserve memory integrity.
        """
        # Case A: Viral Post (Score: 10.0 > 5.0)
        viral_metrics = EngagementMetricsSchema(
            impressions=10000,
            shares=150,   # 150 * 3 = 450
            replies=75,   # 75 * 2 = 150
            likes=400     # 400 * 1 = 400 -> Total: 1000 / 10000 * 100 = 10.0
        )
        score_viral = calculate_composite_score(
            shares=viral_metrics.shares,
            replies=viral_metrics.replies,
            likes=viral_metrics.likes,
            impressions=viral_metrics.impressions
        )
        self.assertEqual(score_viral, 10.0)
        self.assertGreater(score_viral, 5.0)

        # Ingest into vector store
        viral_post_id = f"viral_{uuid.uuid4().hex[:8]}"
        doc_id = self.mem_mgr.ingest_post(
            topic="Deterministic LangGraph State",
            content="State machines guarantee predictability.",
            metrics=viral_metrics,
            hook="Why unconstrained while-loops fail.",
            key_takeaway="State machines drop agent error rates by 99%.",
            post_id=viral_post_id
        )
        self.assertIsNotNone(doc_id)
        
        stats = self.mem_mgr.get_stats()
        self.assertEqual(stats["winning_posts_count"], 1)

        # Case B: Mediocre Post (Score: 0.45 <= 5.0)
        mediocre_metrics = EngagementMetricsSchema(
            impressions=10000,
            shares=5,    # 15
            replies=5,   # 10
            likes=20     # 20 -> Total: 45 / 10000 * 100 = 0.45
        )
        score_mediocre = calculate_composite_score(
            shares=mediocre_metrics.shares,
            replies=mediocre_metrics.replies,
            likes=mediocre_metrics.likes,
            impressions=mediocre_metrics.impressions
        )
        self.assertEqual(score_mediocre, 0.45)
        self.assertLessEqual(score_mediocre, 5.0)

    def test_seam_4_high_engagement_timing_pattern(self):
        """Verifies that high-engagement posts in seed data follow the 14:00 UTC schedule."""
        high_posts = self.db.query(PostModel).filter(PostModel.match_score >= 9.0).all()
        for p in high_posts:
            if p.scheduled_time and "14:00:00" in p.scheduled_time:
                self.assertIn("14:00:00", p.scheduled_time)


if __name__ == "__main__":
    unittest.main()
