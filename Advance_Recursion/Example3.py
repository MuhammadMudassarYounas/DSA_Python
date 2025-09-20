from typing import List

class Solution:
    def solve(self, index, total, subset, nums, target, result):
        if total == target:
            result.append(subset.copy())
            return
        if total > target:
            return
        if index >= len(nums):
            return
        subset.append(nums[index])
        self.solve(index, total + nums[index], subset, nums, target, result)
        subset.pop()
        self.solve(index + 1, total, subset, nums, target, result)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(0, 0, [], candidates, target, result)
        return result


if __name__ == "__main__":
    obj = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(obj.combinationSum(candidates, target))
