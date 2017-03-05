

def swapLexOrder(str_, pairs_):
    pairs = set([tuple(sorted(pair)) for pair in pairs_])

    visited = set()
    discovered = set()
    discovered.add(str_)
    lex_max = str_

    while len(discovered) > 0:
        u = discovered.pop()

        for pair in pairs:
            v = str_swap(u, pair[0] - 1, pair[1] - 1)

            if v != u and v not in visited:
                discovered.add(v)

        visited.add(u)
        lex_max = max(lex_max, u)

    return lex_max


def str_swap(str_, i, j):
    return str_[:i] + str_[j] + str_[i+1:j] + str_[i] + str_[j+1:]

