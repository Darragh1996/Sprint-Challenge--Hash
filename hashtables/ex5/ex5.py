def finder(files, queries):
    matches = []
    cache = {}
    for path in files:
        arr = path.split("/")
        if arr[-1] in cache and path not in cache[arr[-1]]:
            cache[arr[-1]].append(path)
        else:
            cache[arr[-1]] = [path]
    for query in queries:
        if query in cache:
            for i in cache[query]:
                matches.append(i)
    return matches


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
