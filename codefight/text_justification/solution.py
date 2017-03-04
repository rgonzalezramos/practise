def textJustification(words, L):
    return [line for line in justify_lines(words, L)]


def justify_lines(words, L):
    line = []

    for word in words:
        nwords = nspaces = len(line)
        nchars = sum(map(len, line)) + len(word)

        if nspaces + nchars > L:
            if nwords == 1:
                yield right_padding_line(line, L)
            else:
                yield inner_padding_line(line, L)

            line = []

        line.append(word)

    yield right_padding_line(line, L)


def right_padding_line(words, L):
    line = words[0]

    for word in words[1:]:
        line += ' '
        line += word

    line += ' ' * (L - len(line))

    return line


def inner_padding_line(words, L):
    npairs = len(words) - 1
    nchars = sum(map(len, words))
    nspaces = L - nchars
    avg_space_count = nspaces / npairs
    extra_spaces = nspaces % npairs
    regular_spacing = ' ' * avg_space_count

    line = ''
    for i in xrange(npairs):
        line += words[i]
        line += regular_spacing
        if i < extra_spaces:
            line += ' '
    line += words[-1]

    return line

