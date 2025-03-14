def sortArray(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        """
        Insertion Sort
        for i in range(len(nums)):
            j = i
            while j > 0 and nums[j-1] > nums[j]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j = j-1
        """

        for end in range(len(nums)-1, 0, -1):
            i = 0
            j = 1

            while j <= end:
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1

        return nums

print(sortArray([2, 8, 5, 3, 9, 4, 1]))

def merge(arr1, arr2):
        one = 0
        two = 0
        sorted_arr = []

        while one < len(arr1) and two < len(arr2):
            if arr1[one] <= arr2[two]:
                sorted_arr.append(arr1[one])
                one += 1
            else:
                sorted_arr.append(arr2[two])
                two += 1
        
        if one < len(arr1):
            sorted_arr.extend(arr1[one:])

        if two < len(arr2):
            sorted_arr.extend(arr2[two:])
        
        return sorted_arr

arr1 = [1,3,5,7,10,12,14]
arr2 = [2,4,6,8]
print(merge(arr1, arr2))

def mergeSort(nums):
     if len(nums) <= 1:
            return nums
     
     middle = len(nums) // 2
     return merge(mergeSort(nums[0:middle]),mergeSort(nums[middle:]))

print(mergeSort([2, 8, 5, 3, 9, 4, 1]))

def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beginning = 0
        end = len(nums)
        while end - beginning >= 1:
            middle = (beginning + end) // 2

            if target == nums[middle]: 
                return middle
            elif target < nums[middle]:
                end = middle
            elif target > nums[middle]:
                beginning = middle + 1
            
        return -1

print(search([-1,0,3,5,9,12], 9))

def rSearch(nums, target, left, right):
        if left == right:
            return -1
        
        if right - left == 1:
            if nums[left] == target:
                return left
            else:
                return -1
        
        middle = (right + left) // 2

        if target == nums[middle]:
            return middle
        elif target < nums[middle]:
            return rSearch(nums, target, left, middle)
        elif target > nums[middle]:
            return rSearch(nums, target, middle + 1, right)

arr = [-1,0,3,5,9,12,25]
print(rSearch(arr, 2, 0, len(arr)))

#Dynamic Sliding Windows
def smallestSubArray(nums, target):
    sum = nums[0]
    smallest_size = float("inf")
    left = 0
    right = 0

    while right < len(nums)-1:
        # If current sum is bigger than or equal to target sum, decrease the size of the window on the left
        if sum >= target:
            current_size = right - left + 1

            if current_size < smallest_size:
                smallest_size = current_size
            
            sum -= nums[left]
            left += 1

        # If current sum is smaller than target sum, increase the size of the window on the right
        elif sum < target:
            right += 1
            sum += nums[right]
        
        if smallest_size == 1:
             return smallest_size
    return smallest_size


print(smallestSubArray([4, 2, 2, 7, 8, 1, 2, 8, 10], 11))


