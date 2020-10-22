# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
def twoSum(nums, target):
    n = len(nums)
    if n:
        for i in range(n - 1):
            for j in range(n - 1, n):
                if nums[i] <= target and nums[j] <= target:
                    if nums[i] + nums[j] == target:
                        return [i, j]
        print('无结果')
    else:
        print('数据为空')


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = int(input('输入目标:'))
    print(twoSum(nums, 9))
