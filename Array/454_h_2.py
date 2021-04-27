class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        n = len(nums1)
        ans = 0
        
        for i in range(n):
            for j in range(n):
                dict1[nums1[i] + nums2[j]] += 1
                
        for i in range(n):
            for j in range(n):
                ans += dict1[-(nums3[i] + nums4[j])]
                
        return ans