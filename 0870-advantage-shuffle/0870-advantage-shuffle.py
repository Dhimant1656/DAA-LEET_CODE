class Solution(object):
    def advantageCount(self, nums1, nums2):
        n = len(nums1)
        nums1.sort()
        order = sorted(range(n), key=nums2.__getitem__, reverse=True)

        res = [0] * n
        left = 0
        right = n - 1

        for idx in order:
            if nums1[right] > nums2[idx]:
                res[idx] = nums1[right]
                right -= 1
            else:
                res[idx] = nums1[left]
                left += 1

        return res