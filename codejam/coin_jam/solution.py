def optimistic_divisor(n):
    if n <= 1:
        return None
    if n <= 3:
        return None
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5

    # The optimistic trick. If we dont find a divisor smaller
    # than a thousand we surrender and consider it prime
    while (i * i) <= n and i < 1000:
        if n % i == 0:
            return i
        if n % (i + 2) == 0:
            return i + 2
        i += 6

    return None


def candidates(desired_length, string):
    if len(string) == desired_length:
        yield string + '1'

    else:
        for left in candidates(desired_length, string + '0'):
            yield left

        for right in candidates(desired_length, string + '1'):
            yield right


def solutions(length, number_of_coins):
    coins_found = 0

    for candidate in candidates(length, '1'):
        divisors = [optimistic_divisor(int(candidate, base)) for base in xrange(2, 11)]

        if all(divisors):
            coins_found += 1
            yield (candidate, divisors,)

            if coins_found == number_of_coins:
                break


if __name__ == '__main__':
    raw_input() # Skip number of lines

    length, number_of_coins = map(int, raw_input().split(' '))

    for coin, divisors in solutions(length, number_of_coins):
        print '%s %s' % (coin, ' '.join(map(str, divisors)))

