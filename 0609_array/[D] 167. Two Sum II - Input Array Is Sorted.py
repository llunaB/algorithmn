class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        "two pointer 활용"

        l, r = 0, len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
