def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """
    NUM_PER_BUS = 50
    if n % NUM_PER_BUS == 0:
        return n / NUM_PER_BUS 
    else:
        return (n / NUM_PER_BUS) + 1


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """
    pos = 0
    neg = 0
    for each in price_changes:
        if each >= 0:
            pos += each
        else:
            neg += each
    return (pos, neg)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """

    if len(L) ==0:
        return "Nothing to swap!"
    elif len(L) == k:
        return L
    else:
        for i in range(k):
            swap1 = L.pop(i)
            swap2 = L.pop(-i + -1)
            L.insert(0, swap2)
            L.append(swap1)
    return L


if __name__ == '__main__':
    import doctest
    doctest.testmod()
