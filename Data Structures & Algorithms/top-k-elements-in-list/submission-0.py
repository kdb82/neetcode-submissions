class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        k_common = counts.most_common(k)

        solution = []
        for tup in k_common:
            solution.append(tup[0])

        return solution