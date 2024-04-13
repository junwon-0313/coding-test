def permutations(array, r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            for next in permutations(array[:i]+array[i+1:],r-1):
                yield [array[i]] + next

print(list(permutations([1,2,3,4],2)))

def combinations(array, r):
    for i in range(len(array)):
        if r==1:
            yield [array[i]]
        else:
            for next in combinations(array[i+1:],r-1):
                yield [array[i]] + next

print(list(combinations([1,2,3,4],2)))
