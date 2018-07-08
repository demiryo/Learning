"""

1. Two Sum

https://leetcode.com/problems/two-sum/description/

Given an array of integers, return True if there exists a pair that make up the sum.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return True : [0, 1].


"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        # for i in nums:
        #   num = i
        N = len(nums)
        for i in range(N):
            num1 = nums[i]
            for j in range(i+1, N):
                num2=nums[j]
                if num1 + num2 == target:
                    return True
        return False


class TestSolution(object):
    def __init__(self):
        self.solution = Solution()

    def run(self, nums, target, expected):
        actual = self.solution.twoSum(nums, target)
        if (actual != expected):
            print("Test ([{}], {}) = {} (( FAILED )) : expected {}".format(nums, target, actual, expected))
        else:
            print("Test ([{}], {}) = {} (( PASSED )) ".format(nums, target, actual))


test = TestSolution()
test.run(nums=[2, 7, 11, 15], target=9, expected=True)
test.run(nums=[2, 7, 11, 15], target=8, expected=False)
test.run(nums=[10, 5, 3, 2], target=5, expected=True)
test.run(nums=[10, 5, 3, 2], target=4, expected=False)
test.run(nums=[2], target=5, expected=False)
test.run(nums=[5], target=5, expected=False)
test.run(nums=[], target=5, expected=False)
test.run(nums=[3,2], target=5, expected=True)
