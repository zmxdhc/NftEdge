# test_nftedge.py
"""
Tests for NftEdge module.
"""

import unittest
from nftedge import NftEdge

class TestNftEdge(unittest.TestCase):
    """Test cases for NftEdge class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftEdge()
        self.assertIsInstance(instance, NftEdge)

    def test_run_method(self):
        """Test the run method."""
        instance = NftEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
