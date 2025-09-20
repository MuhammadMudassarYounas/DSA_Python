def Combination(candidates, target):
    Result = []
    candidates.sort()

    def backtrack(index, total, subset):
        if total == 0:
            Result.append(subset.copy())
            return
        if total < 0:
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            subset.append(candidates[i])
            backtrack(i + 1, total - candidates[i], subset)
            subset.pop()

    backtrack(0, target, [])
    return Result

print(Combination([1, 1, 2, 1, 2], 3))
