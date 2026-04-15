class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i1, i2, k = m-1, n-1, m+n-1
        while i2>=0:
            if i1>=0 and nums1[i1]>nums2[i2]:
                nums1[k] = nums1[i1]
                k -= 1
                i1 -= 1
            else:
                nums1[k] = nums2[i2]
                k -= 1
                i2 -= 1