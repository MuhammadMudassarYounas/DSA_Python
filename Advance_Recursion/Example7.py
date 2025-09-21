def LetterCombination(digits):
    char_Map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    result = []
    def Backtrack(index, subset):
        if index >= len(digits):
            result.append("".join(subset))
            return
        for ch in char_Map[digits[index]]:
            subset.append(ch)
            Backtrack(index+1, subset)
            subset.pop()
    if digits:
        Backtrack(0, [])
    return result

print(LetterCombination("26"))
