class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        frequencies = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        for num, count in counts.items():
            frequencies[count].append(num)
        
        res = []

        for i in range(len(frequencies)-1, 0, -1):
            for c in frequencies[i]:
                res.append(c)
                if len(res) == k:
                    return res