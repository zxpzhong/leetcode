#
# @lc app=leetcode.cn id=93 lang=python
#
# [93] 复原IP地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (45.46%)
# Likes:    188
# Dislikes: 0
# Total Accepted:    24.3K
# Total Submissions: 53.4K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
# 
# 示例:
# 
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
# 
#

# @lc code=start
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 返回的是所有可能的IP地址格式，IP地址每一个范围为0-255一共256个数
        # 换个问法就是一个字符串有多少种可以被分割为四个0-256的分法
        self.ans = []
        self.split_one(s,[],0)
        return [temp[0]+'.'+temp[1]+'.'+temp[2]+'.'+temp[3] for temp in self.ans]

    def split_one(self,str,ans,time):
        if time == 4:
            if len(str) == 0:
                # 次数为4且无字符剩余退出
                self.ans.append(ans)
            else:
                return
        # 判断当前最少需要分掉的字符
        # 假设第一个地址，最少需要分配字符数为：len(str)-3*3
        min_length = max(1,len(str)-(3-time)*3)
        for i in range(min_length,min(len(str),3)+1):
            if int(str[:i]) < 256:
                if i > 1 and str[0] == '0':
                    return
                self.split_one(str[i:],ans+[str[:i]],time+1)
            else:
                break
        
        
# @lc code=end

s = "010010"

solu = Solution()
print(solu.restoreIpAddresses(s))