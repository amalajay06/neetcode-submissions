import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rank=Counter(nums)
        kkeys=heapq.nlargest(k,rank,key=rank.get)
        return kkeys