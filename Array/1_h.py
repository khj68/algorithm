def twoSum(self, nums, target: int):
        left, right = 0, 1
        nums = [ (x, i) for i, x in enumerate(nums) ]
        nums.sort(key=lambda x: x[0])
        print(nums)
        while left != right and right < len(nums):
            cur = nums[left][0] + nums[right][0]
            if cur == target:
                return [nums[left][1], nums[right][1]]
            elif cur < target:
                right += 1
            else:
                left += 1
        print(left, right)


twoSum(0, [3,2,3], 6)