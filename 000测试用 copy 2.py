class Solution:
    def minNumber(self, nums):
        def smaller(a,b):
            pass
            temp1 = str(a)
            temp2 = str(b)
            length = min(len(temp1),len(temp2))
            for i in range(length):
                if int(temp1[i]) > int(temp2[i]):
                    return False
                elif int(temp1[i]) < int(temp2[i]):
                    return True
            if len(temp1) == len(temp2):
                return True
            if len(temp1)<len(temp2) and temp2[i+1] == '0':
                return False
            if len(temp1)>len(temp2) and temp1[i+1] == '0':
                return True
            
            # 小于=返回True
            # 大于返回False

        
        # 对数字进行排序
        # 快排
        def quick_sort(i,j):
            if i >= j : return 
            left = i-1
            right = j+1
            mid = (left+right)//2
            # while left <= j and right >= i and left < right:
            while left < right:
                left+=1
                while smaller(nums[left],nums[mid]):
                    left+=1
                    # continue
                right-=1
                while not smaller(nums[right],nums[mid]):
                    right-=1
                    # continue
                if left < right:
                    # left和right对应的交换
                    temp = nums[left]
                    nums[left] = nums[right]
                    nums[right] = temp
                
            quick_sort(i,right)
            quick_sort(right+1,j)

        nums.sort()
        quick_sort(0,len(nums)-1)

        print(nums)

solu = Solution()
print(solu.minNumber([10,2,20]))        
# print(smaller(2,20))
        