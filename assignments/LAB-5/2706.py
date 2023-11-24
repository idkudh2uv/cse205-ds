class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        heapify(prices)
        sm = heappop(prices)+heappop(prices)
        return money - sm if sm <= money else money