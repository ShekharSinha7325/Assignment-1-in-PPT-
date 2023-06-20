#  Q1 



from ast import List


class solution:
    def twoSum(self, nums: list[int],target :int)->list[int]:
        for i in range (len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return([i,j])
                
# Q2.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[count] = nums[i]
            count += 1
        
        return count
    
# Q3
class Solution:
   def searchInsert(self, nums: List[int], target: int) -> int:
        if nums==[]:
            return 0
        l = len(nums)
        i= 0
        j= l-1
        if target > nums[j]:
            return l
        elif target<nums[i]:
            return 0
        while (i<=j):
    
            mid = i + ((j-i)//2)        
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                j=mid-1
            elif target > nums[mid]:
                i=mid+1
        return i
# Q4
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0
        return [1]+[0]*len(digits)

# Q5
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=0
        for x in range(len(nums1)):
            if i>=n:
                break
            if nums1[x]==0:
                nums1[x]=nums2[i]
                i+=1           
        nums1.sort()
# Q6
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return (len(nums)!=len(set(nums)))
# Q7
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if(nums[i]==0):
                nums.remove(nums[i])
                nums.append(0)
            else:
                continue
# Q8
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N, dupe = len(nums), 0
        seen, sumN = [0] * (N+1), N * (N+1) // 2
        for num in nums:
            sumN -= num
            if seen[num]: dupe = num
            seen[num] += 1
        return [dupe, sumN + dupe]