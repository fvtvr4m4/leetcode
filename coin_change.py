# https://leetcode.com/problems/coin-change/












# non-dp solution: works only if coins array is sorted
# class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
        # count = 0
        # for i in range(len(coins)-1, -1, -1):
            # if coins[i] < amount:
                # while amount - coins[i] >= 0:
                    # count += 1
                    # amount -= coins[i]
                # if amount == 0:
                    # break
                # else:
                    # continue
            # elif coins[i] == amount:
                # return count + 1
            # else:
                # continue
        # if amount == 0:
            # return count
        # else:
            # return -1
