def get_indices_of_item_weights(weights, length, limit):
    weight_cache = {}
    for i in range(0, length):
        difference = limit - weights[i]
        if difference in weight_cache:
            return (i, weight_cache[difference])
        else:
            weight_cache[weights[i]] = i
    return None
