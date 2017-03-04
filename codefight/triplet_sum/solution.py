def tripletSum(x, a):
    a.sort()
    n = len(a)

    last_possible_start_value = x / 3
    last_possible_start_index = n - 2
    start = 0

    while a[start] <= last_possible_start_value and start <= last_possible_start_index:
        middle = start + 1
        end = n - 1

        while middle < end:
            sum_ = a[start] + a[middle] + a[end]

            if sum_ > x:    end -= 1
            elif sum_ < x:  middle += 1
            else:           return True

        start += 1

    return False

