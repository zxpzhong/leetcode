# n,x = map(int, input().split())
# nums = list(map(int,input().split()))
# nums.sort()
# # import copy

# # nums = copy.deepcopy(nums2)
# # nums = list(set(nums))
# n = len(nums)

# pt1 = 0
# pt2 = n-1


# # while True:
# while nums[pt2]-nums[pt1] > x:
#     if nums[pt1+1]-nums[pt1] > nums[pt2]-nums[pt2-1]:
#         pt1+=1
#     else:
#         pt2-=1
#     # pt1和pt2差值小于x了
# # print(pt1+n-1-pt2)
# # 拓展
# flag = 0
# while nums[pt2]-nums[pt1] <= x and pt1>0 and pt2<n-1:
#     if nums[pt2+1]-nums[pt2] < nums[pt1]-nums[pt1-1]:
#         pt2+=1
#         flag = 1
#     else:
#         pt1-=1
#         flag = 2

# if flag == 0:
#     print(pt1+n-1-pt2)
# elif flag == 1:
#     print(pt1+n-1-pt2-1)
# elif flag == 2:
#     print(pt1+n-1-pt2+1)



n,x = map(int, input().split())
nums = list(map(int,input().split()))
nums.sort()
if nums[-1]-nums[0] <=x:
    print(0)
else:
    n = len(nums)
    max_len = 0
    for i in range(n):
        for j in range(i,n):
            if nums[j]-nums[i] <= x:
                max_len = max(max_len,j-i+1)
    print(n-max_len)


