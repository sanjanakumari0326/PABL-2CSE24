class Solution:
    def minimumNumberOfSwaps(self, s):
        countLeft = 0
        countRight = 0
        imbalance = 0
        swaps = 0

        for ch in s:
            if ch == '[':
                countLeft += 1

                if imbalance > 0:
                    swaps += imbalance
                    imbalance -= 1
            else:
                countRight += 1
                imbalance = countRight - countLeft

        return swaps

s = "[]][]["

obj = Solution()
print(obj.minimumNumberOfSwaps(s))