class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Initialize three pointers
        i = m - 1  
        j = n - 1
        k = m + n - 1

        # Loop from back-to-front to avoid overwriting uncompared integers
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # Drain if there are any remaining values in num2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
    