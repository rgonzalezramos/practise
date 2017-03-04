#!/usr/bin/env python

import sys


INF = sys.maxint


def wordLadder(begin_word, end_word, approved_words):
    # Fail fast if it's clearly impossible
    if not end_word in approved_words: return 0

    # Build the word list for the graph
    if begin_word in approved_words:
        word_list = approved_words
    else:
        word_list = [begin_word] + approved_words

    i_begin_word = word_list.index(begin_word)
    i_end_word = word_list.index(end_word)

    graph = build_adjacency_matrix(word_list)
    dist = dijkstra_distance(graph, i_begin_word)

    # We have to return number of vertices != first, and dijkstra_distances returns
    # number of edges
    return dist[i_end_word] + 1 if dist[i_end_word] != INF else 0


def build_adjacency_matrix(word_list):
    nwords = len(word_list)

    graph = []
    for i in xrange(nwords):
        graph.append([])
        for j in xrange(nwords):
            lv_distance = levenshtain_distance(word_list[i], word_list[j])
            graph[i].append(lv_distance if lv_distance <= 1 else INF)

    return graph


def levenshtain_distance(word_a, word_b):
    ''' Calculates Levenshtain distance for equally sized words '''
    assert len(word_a) == len(word_b), 'This method only works for words of equal size'

    nchars = len(word_a)
    distance = 0
    for i in xrange(nchars):
        if word_a[i] != word_b[i]:
            distance += 1

    return distance


def dijkstra_distance(graph, source):
    nvertices = len(graph)
    dist = [INF] * nvertices
    visited = [False] * nvertices

    dist[source] = 0

    while True:
        u = min_distance_vertex(dist, visited)

        # We visited all the connected vertices
        if u is None: break

        visited[u] = True

        for v in xrange(nvertices):
            # if v not visited and u -> v exists and path(src, u) + path(u, v) is current shortest path(src, v)
            if not visited[v] and graph[u][v] and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    return dist


def min_distance_vertex(dist, visited):
    ''' Index for reachable non visited vertex of minimum distance '''
    i_min = None
    min_distance = INF

    for v in xrange(len(dist)):
        if not visited[v] and dist[v] < min_distance:
            min_distance = dist[v]
            i_min = v

    return i_min


if __name__ == '__main__':
    print wordLadder('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])
