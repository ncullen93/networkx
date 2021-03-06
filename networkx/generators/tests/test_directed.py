"""Generators - Directed Graphs
----------------------------
"""
from nose.tools import assert_equal
from nose.tools import assert_raises
from nose.tools import assert_true

import networkx
from networkx.classes import Graph
from networkx.classes import MultiDiGraph
from networkx.generators.directed import gn_graph
from networkx.generators.directed import gnr_graph
from networkx.generators.directed import gnc_graph
from networkx.generators.directed import random_k_out_graph
from networkx.generators.directed import scale_free_graph


class TestGeneratorsDirected(object):
    def test_smoke_test_random_graphs(self):
        gn_graph(100)
        gnr_graph(100, 0.5)
        gnc_graph(100)
        scale_free_graph(100)

    def test_create_using_keyword_arguments(self):
        assert_raises(networkx.exception.NetworkXError,
                      gn_graph, 100, create_using=Graph())
        assert_raises(networkx.exception.NetworkXError,
                      gnr_graph, 100, 0.5, create_using=Graph())
        assert_raises(networkx.exception.NetworkXError,
                      gnc_graph, 100, create_using=Graph())
        assert_raises(networkx.exception.NetworkXError,
                      scale_free_graph, 100, create_using=Graph())
        G=gn_graph(100,seed=1)
        MG=gn_graph(100,create_using=MultiDiGraph(),seed=1)
        assert_equal(sorted(G.edges()), sorted(MG.edges()))
        G=gnr_graph(100,0.5,seed=1)
        MG=gnr_graph(100,0.5,create_using=MultiDiGraph(),seed=1)
        assert_equal(sorted(G.edges()), sorted(MG.edges()))
        G=gnc_graph(100,seed=1)
        MG=gnc_graph(100,create_using=MultiDiGraph(),seed=1)
        assert_equal(sorted(G.edges()), sorted(MG.edges()))


class TestRandomKOutGraph(object):
    """Unit tests for the
    :func:`~networkx.generators.directed.random_k_out_graph` function.

    """

    def test_regularity(self):
        """Tests that the generated graph is ``k``-out-regular."""
        n = 10
        k = 3
        alpha = 1
        G = random_k_out_graph(n, k, alpha)
        assert_true(all(d == k for v, d in G.out_degree()))

    def test_no_self_loops(self):
        """Tests for forbidding self-loops."""
        n = 10
        k = 3
        alpha = 1
        G = random_k_out_graph(n, k, alpha, self_loops=False)
        assert_equal(G.number_of_selfloops(), 0)
