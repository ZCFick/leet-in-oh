#My Solution
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts: dict[int, int] = {}
        maj = -1
        m = 0
        for x in nums:
            counts[x] = counts.get(x, 0) + 1
            if maj == x:
                m += 1
            else:
                if counts[x] > m:
                    m = counts[x]
                    maj = x
        return maj
    
#Optimal Solution using Boyer-More Voting Algorithm
class Solution:
    def majorityElement(self, nums: list[int]):

        candidate = 0
        count = 0

        for num in nums:

            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            else:
                count -= 1

        return candidate
