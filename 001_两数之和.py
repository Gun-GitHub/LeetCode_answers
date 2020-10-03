# 1.两数之和
#   给定一个整数数组
# nums
#   和一个目标值
# target
#   请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#
#
# 示例:
#   给定
#       nums = [2, 7, 11, 15], target = 9
#   因为
#       nums[0] + nums[1] = 2 + 7 = 9
#       所以返回[0, 1]


class Solution(object):

    def twoSum(self, nums: list, target: int, need_all_possibility: bool = False) -> list:
        soucerList = list(nums)
        nums.sort()
        if nums[0] < 0:
            top = self.dichotomizing_search(nums, target - nums[0], exact=False)
            bottom = self.dichotomizing_search(nums, int(target / 2), exact=False)
        else:
            top = self.dichotomizing_search(nums, target, exact=False)
            bottom = self.dichotomizing_search(nums, int(target / 2), exact=False)
        if top == -1:
            return [None, None]
        all_possibility = []
        if top < bottom:
            top, bottom = bottom, top
        for i in range(bottom, top + 1):
            another_num = target - nums[i]
            the_bottom = bottom
            another_num_index = self.dichotomizing_search(nums[0:the_bottom + 1], another_num)
            if another_num_index != -1:
                if need_all_possibility:
                    if another_num_index == i:
                        pass
                    elif nums[another_num_index] == nums[i]:
                        all_possibility.append(
                            [
                                soucerList.index(nums[another_num_index]),
                                soucerList.index(
                                    nums[i],
                                    soucerList.index(nums[another_num_index]) + 1
                                )
                            ]
                        )
                    else:
                        all_possibility.append(
                            [
                                soucerList.index(nums[another_num_index]),
                                soucerList.index(nums[i])
                            ]
                        )
                else:
                    if another_num_index == i:
                        pass
                    elif nums[another_num_index] == nums[i]:
                        return [
                            soucerList.index(nums[another_num_index]),
                            soucerList.index(nums[i], soucerList.index(nums[another_num_index]) + 1)
                        ]
                    else:
                        return [
                            soucerList.index(nums[another_num_index]),
                            soucerList.index(nums[i])
                        ]
        return all_possibility

    def dichotomizing_search(self, targetList: list, targetNum: int, exact: bool = True) -> int:
        cursor_min = 0
        cursor_max = len(targetList) - 1
        if cursor_max == -1:
            cursor_max = 0
        cursor_mid = int((cursor_max + cursor_min) / 2)
        while True:
            if targetList[cursor_min] > targetNum:
                if targetList[cursor_min] < 0 and targetNum < 0:
                    return cursor_max
                else:
                    return -1
            if targetList[cursor_max] < targetNum:
                if exact:
                    return -1
                else:
                    return cursor_max
            if targetList[cursor_mid] == targetNum:
                return cursor_mid
            if targetList[cursor_mid] > targetNum:
                cursor_max = cursor_mid
                cursor_mid = int((cursor_max + cursor_min) / 2)
            if targetList[cursor_mid] < targetNum:
                cursor_min = cursor_mid
                cursor_mid = int((cursor_max + cursor_min) / 2)
            if cursor_max - cursor_min == 1 or cursor_max == cursor_min:
                if exact:
                    if targetList[cursor_max] == targetNum:
                        return cursor_max
                    elif targetList[cursor_min] == targetNum:
                        return cursor_min
                    else:
                        return -1
                else:
                    return cursor_max


if __name__ == '__main__':
    nums = [0,3,-3,4,-1]
    target = -1
    result = Solution().twoSum(nums, target)
    print(result)
