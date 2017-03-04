def treeLevelSum(tree, k):
    current_level = -1
    values_at_level_k = 0
    last_number_string = ''

    for char in tree:
        if char == '(':
            # We can parse the number when opening a new node
            # since leaf nodes are (<NUMBER>()())
            if current_level == k and last_number_string:
                values_at_level_k += int(last_number_string)
            last_number_string = ''
            current_level += 1
        elif char == ')':
            current_level -= 1
        else:
            last_number_string += char

    return values_at_level_k

