def removeDuplicates(self, nums) -> int:
        new_tail = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[new_tail]:
                new_tail += 1
                nums[new_tail] = nums[i]
            print(i, nums, new_tail)
                
        return new_tail + 1

removeDuplicates(0, [0,0,1,1,1,2,2,3,3,4])