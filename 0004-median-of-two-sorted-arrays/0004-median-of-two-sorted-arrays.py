from bisect import bisect_right as br
from bisect import bisect_left as bl
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        half = (m+n+1)/2
        left = -10**6
        right = 10**6
        if (m+n) % 2:            
            while left < right:
                mid = (left + right) // 2
                right_curr = br(nums1, mid) + br(nums2, mid)
                left_curr = bl(nums1, mid) + bl(nums2, mid)
                if right_curr >= half:
                    if left_curr < half:
                        return mid
                    else:
                        right = mid - 1
                else:
                    left = mid + 1
            mid = (left + right) // 2
            right_curr = br(nums1, mid) + br(nums2, mid)
            left_curr = bl(nums1, mid) + bl(nums2, mid)
            return left
        else:
            while left < right:
                mid = (left + right) // 2
                right_curr = br(nums1, mid) + br(nums2, mid)
                left_curr = bl(nums1, mid) + bl(nums2, mid)
                if right_curr >= half:
                    if left_curr < half-1:
                        return mid
                    else:
                        right = mid
                else:
                    left = mid + 1
            mid = (left + right) // 2
            right_curr = br(nums1, mid) + br(nums2, mid)
            left_curr = bl(nums1, mid) + bl(nums2, mid)
            if left_curr > half - 1:
                i1 = bl(nums1, mid)
                i2 = bl(nums2, mid)
                other = -10**6
                if i1:
                    other = nums1[i1-1]
                if i2:
                    other = max(other, nums2[i2-1])
                return (left + other) /2
            else:
                i1 = br(nums1, mid)
                i2 = br(nums2, mid)
                other = 10**6
                if i1 < m:
                    other = nums1[i1]
                if i2 < n:
                    other = min(other, nums2[i2])
                return (left + other) /2
