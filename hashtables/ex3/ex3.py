def intersection(arrays):
    inter_cache = {}
    intersection_arr = []
    for i in range(0, len(arrays)):
        for j in arrays[i]:
            if j in inter_cache:
                inter_cache[j] += 1
            else:
                inter_cache[j] = 1
    for key in inter_cache:
        if inter_cache[key] == len(arrays):
            intersection_arr.append(key)
    return intersection_arr


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
    # arrays2 = []
    # arrays2.append([1, 2, 3])
    # arrays2.append([1, 4, 5])
    # arrays2.append([1, 6, 7])
    # print(intersection(arrays2))
