from collections import deque

def solve(n, k, nums):
    # 最小的数
    max_nums, min_nums = [nums[0]], [nums[0]]
    # 最小的索引
    min_queue, max_queue = deque([0]), deque([0])
    for i in range(1, n):
        # 最小的索引如果过去了，弹出
        while min_queue and min_queue[0] + k <= i:
            min_queue.popleft()
        # 最大的索引如果过去了，就弹出
        while max_queue and max_queue[0] + k <= i:
            max_queue.popleft()
        # 最小的索引还有，并且找到新的元素nums[i]的位置
        while min_queue and nums[min_queue[-1]] >= nums[i]:
            min_queue.pop()
        while max_queue and nums[max_queue[-1]] <= nums[i]:
            max_queue.pop()
        
        min_queue.append(i)
        max_queue.append(i)
        # print([nums[x] for x in min_queue], [nums[x] for x in max_queue])
        min_nums.append(nums[min_queue[0]])
        max_nums.append(nums[max_queue[0]])
    # print(min_nums, max_nums)
    return min_nums[k-1:], max_nums[k-1:]


n, k = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
# print(n,k)
# print(nums)
min_nums, max_nums = solve(n, k, nums)
print(' '.join([str(x) for x in min_nums]))
print(' '.join([str(x) for x in max_nums]))