class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) <= len(nums2):
            smaller = nums1
            larger = nums2
        else:
            smaller = nums2
            larger = nums1
        left = 0
        right = len(smaller)
        while left <= right:
            i = (left + right) / 2
            j = (len(smaller) + len(larger) - 2 * i) / 2
            if i != 0 and j != len(larger) and smaller[i - 1] > larger[j]:
                right = i
            elif j != 0 and i != len(smaller) and larger[j - 1] > smaller[i]:
                left = i + 1
            else:
                candidates = []
                if i != len(smaller):
                    candidates.append(smaller[i])
                if j != len(larger):
                    candidates.append(larger[j])
                second = min(candidates)
                # Odd
                if (len(smaller) + len(larger)) % 2:
                    return second
                # Even
                else:
                    candidates = []
                    if i:
                        candidates.append(smaller[i - 1])
                    if j:
                        candidates.append(larger[j - 1])
                    first = max(candidates)
                    return (first + second) / 2.0