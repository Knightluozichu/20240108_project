# lst = [1, 2, 3,4]
# for i in lst:
#     # print(i)
#     lst.remove(i)
# print(lst)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        # for n in range(len(nums)):
            # print(n, nums[n])
        while i < len(nums):
            for n in range(len(nums)):
                if i <= n:
                    continue
                else:
                    if (nums[i] + nums[n]) == target:
                        return [i, n]
            i += 1

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        r = {}
        e = None
        for n in range(len(nums)):
            e = nums[n]
            r[n] = e
            # print(r)
            sub = target - e
            for k, v in r.items():
                if n == k:
                    continue
                else:
                    if v == sub:
                        # print([n, k])
                        return [n, k]



    def twoSum(self, nums: List[int], target: int)-> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


# 创建Solution类的实例
solution = Solution()

# # 调用f方法
# nums = [3, 2, 4]
# target = 6
# result = solution.twoSum(nums, target)

# print(result)  # 输出：[2, 7]


solution.twoSum2([3, 3], 6)
