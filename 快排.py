# import sys
# n = int(sys.stdin.readline().strip())
# nums = list(map(int,sys.stdin.readline().strip().split()))

# def quick_sort(q, l, r):
#     if l >= r: return
#     i = l - 1
#     j = r + 1
#     # 中间位置
#     x = q[l + r >> 1]
#     while i < j:
#         # 首先找左边大于的
#         i+=1
#         while q[i] < x: i+=1
#         j-=1
#         while q[j] > x: j-=1
#         if i < j: 
#             temp = q[j]
#             q[j] = q[i]
#             q[i] = temp
#     # 左边都是小于的，右边都是大于的，对左右两边分别进行快排
#     # 左边范围为：l,j
#     quick_sort(q, l, j)
#     # 右边范围为：j+1,r
#     quick_sort(q, j + 1, r)

# quick_sort(nums,0,n-1)
# for item in nums:
#     print(item,end=' ')



import sys
n = int(sys.stdin.readline().strip())
nums = list(map(int,sys.stdin.readline().strip().split()))

def quick_sort(i,j):
    if i >= j: return
    p = i-1
    q = j+1
    mid = nums[p+q>>1]
    while p < q:
        p+=1
        while nums[p] < mid:
            p+=1
        q-=1
        while nums[q] > mid:
            q-=1
        if p<q:
            temp = nums[q]
            nums[q] = nums[p]
            nums[p] = temp
    quick_sort(i,q)
    quick_sort(q+1,j)
quick_sort(0,n-1)
for item in nums:
    print(item,end=' ')