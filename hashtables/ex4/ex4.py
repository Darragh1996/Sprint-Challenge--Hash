def has_negatives(a):
    cache = {}
    pairs = []
    for i in a:
        num = i
        if num < 0:
            num *= -1
        if num in cache:
            pairs.append(num)
        else:
            cache[num] = 1
    return pairs


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
