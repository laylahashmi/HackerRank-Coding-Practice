def matchingStrings(strings, queries):
    occurences = {}
    result = []
    for i in strings:
        if i not in occurences:
            occurences[i] = 0
        occurences[i] += 1

    for i in queries:
        if i in occurences:
            result.append(occurences[i])
        if i not in occurences:
            result.append(0)

    return result


print(matchingStrings(["aba", "ba", "aba", "xzb"], ["aba", "xzb", "baba"]))
