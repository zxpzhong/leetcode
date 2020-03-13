#
# @lc app=leetcode.cn id=401 lang=python
#
# [401] 二进制手表
#
# https://leetcode-cn.com/problems/binary-watch/description/
#
# algorithms
# Easy (49.39%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    11.4K
# Total Submissions: 22K
# Testcase Example:  '0'
#
# 二进制手表顶部有 4 个 LED 代表小时（0-11），底部的 6 个 LED 代表分钟（0-59）。
# 
# 每个 LED 代表一个 0 或 1，最低位在右侧。
# 
# 
# 
# 例如，上面的二进制手表读取 “3:25”。
# 
# 给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。
# 
# 案例:
# 
# 
# 输入: n = 1
# 返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16",
# "0:32"]
# 
# 
# 
# 注意事项:
# 
# 
# 输出的顺序没有要求。
# 小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
# 分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。
# 
# 
#

# @lc code=start
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        # 根据亮着LED数目，给出输出的时间
        # 从num中选择i个作为小时刻度，剩余num-i个作为分钟刻度
        # 时钟部位最大为4颗LED,最小为num-6颗，如果num》6
        hour_min = max(num-6,0)
        hour_max = min(num,3)
        # 小时候选
        hours = []
        hours.append(['0'])
        hours.append(['1','2','4','8'])
        hours.append(['3','5','6','9','10'])
        hours.append(['7','11'])
        # hours.append(['15'])
        # 分钟候选
        mins = [[] for _ in range(7)]
        mins[0].append('00')
        def get_1num(s):
            count = 0
            for i in range(len(s)):
                if s[i] == '1':
                    count+=1
            return count
        for i in range(1,60):
            temp = str(i)
            temp = temp if len(temp)==2 and not temp[:-1] == '0' else '0'+temp
            mins[get_1num(bin(i)[2:])].append(temp)
        ans = []
        for i in range(hour_min,hour_max+1):
            # 当前选中了i+1颗时钟LED，可以表示C 4 i+1种时间
            # 剩余的num-i颗LED表示分钟，可以表示C6 num-i种分钟时间
            temp1 = hours[i]
            temp2 = mins[num-i]
            # temp1 2 组合
            for item1 in temp1:
                for item2 in temp2:
                    ans.append(item1+':'+item2)
        return ans
            
# @lc code=end

solu = Solution()
print(solu.readBinaryWatch(3))