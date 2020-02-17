#
# @lc app=leetcode.cn id=42 lang=python
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (46.43%)
# Likes:    816
# Dislikes: 0
# Total Accepted:    49.2K
# Total Submissions: 102.2K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def get_max(height,flag = 0):
            max_index = []
            length = len(height)
            for i in range(length):
                if i == 0:
                    if height[0]> height[1] or flag == 1:
                        max_index.append(0)
                elif i == length-1:
                    if height[-1]>height[-2] or flag == 1:
                        max_index.append(length-1)
                elif (height[i]>height[i+1] and height[i]>height[i-1]) or (height[i]==height[i+1] and height[i]>height[i-1])or (height[i]>height[i+1] and height[i]==height[i-1]): 
                    max_index.append(i)
            if len(max_index) < 2:
                return []
            return max_index
        def get_max2(height,index):
            max_index = []
            flag = 1
            length = len(height)
            for i in range(length):
                if i == 0:
                    if height[0]> height[1] or flag == 1:
                        max_index.append(0)
                elif i == length-1:
                    if height[-1]>height[-2] or flag == 1:
                        max_index.append(length-1)
                elif (height[i]>height[i+1] and height[i]>height[i-1]) or (height[i]==height[i+1] and height[i]>height[i-1])or (height[i]>height[i+1] and height[i]==height[i-1]): 
                    max_index.append(i)
            if len(max_index) < 2:
                return None,None
            ret = []
            # 已经找到所有的最大值，检查最大值之间是否存在更小的值，如果有则删除
            for i in range(len(max_index)-1):
                # 取出两个最小值，遍历中间的
                min_height = min(height[max_index[i]],height[max_index[i+1]])
                for j in range(max_index[i]+1,max_index[i+1]):
                    # 中间是否存在比两端更小的值
                    if not height[j] < min_height:
                        ret.append(j)
            ret = ret+max_index
            ret.sort()

            if len(ret) < 2:
                return None,None
            new_index = []
            for i in range(len(ret)):
                new_index.append(index[ret[i]])
            new_height = []
            for i in range(len(ret)):
                new_height.append(height[ret[i]])
            return new_index,new_height

        def get_max3(height):
            # 初始化
            ret = [i for i in range(len(height))]
            new_height = height
            while True:
                pre_ret = ret
                ret,new_height = get_max2(new_height,ret)
                if ret == None:
                    return []
                if pre_ret == ret:
                    break
            return ret
            

        # 1.0 找到所有的局部极大值索引
        length = len(height)
        if length < 2:
            return 0

        max_index = get_max(height)

        # 1.1 去除极大之间的更小的极大(二阶导数求更大)
        new_list = []
        for i in range(len(max_index)):
            new_list.append(height[max_index[i]])
        max_index2 = get_max3(new_list)
        for i in range(len(max_index2)):
            max_index2[i] = max_index[max_index2[i]]

        # 2.0 遍历所有的局部极大值，求取每两个局部极大值之间的雨水值
        sum_ans = 0
        for i in range(len(max_index2)-1):
            min_height = min(height[max_index2[i]],height[max_index2[i+1]])
            for j in range(max_index2[i]+1,max_index2[i+1]):
                sum_ans+=max(0,min_height-height[j])
        return sum_ans
            
# @lc code=end

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# height = [2,0,2]
# height = [5,4,1,2]
# height = [5,2,1,2,1,5]
# height = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
height = [0,2,0]
# height = [6,2,2,9,6,8,5,8,3,7,3,8,9,8,1,2,4]
solu = Solution()
print(solu.trap(height))