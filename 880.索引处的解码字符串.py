#
# @lc app=leetcode.cn id=880 lang=python
#
# [880] 索引处的解码字符串
#
# https://leetcode-cn.com/problems/decoded-string-at-index/description/
#
# algorithms
# Medium (20.14%)
# Likes:    77
# Dislikes: 0
# Total Accepted:    2.2K
# Total Submissions: 9.8K
# Testcase Example:  '"leet2code3"\n10'
#
# 给定一个编码字符串 S。为了找出解码字符串并将其写入磁带，从编码字符串中每次读取一个字符，并采取以下步骤：
# 
# 
# 如果所读的字符是字母，则将该字母写在磁带上。
# 如果所读的字符是数字（例如 d），则整个当前磁带总共会被重复写 d-1 次。
# 
# 
# 现在，对于给定的编码字符串 S 和索引 K，查找并返回解码字符串中的第 K 个字母。
# 
# 
# 
# 示例 1：
# 
# 输入：S = "leet2code3", K = 10
# 输出："o"
# 解释：
# 解码后的字符串为 "leetleetcodeleetleetcodeleetleetcode"。
# 字符串中的第 10 个字母是 "o"。
# 
# 
# 示例 2：
# 
# 输入：S = "ha22", K = 5
# 输出："h"
# 解释：
# 解码后的字符串为 "hahahaha"。第 5 个字母是 "h"。
# 
# 
# 示例 3：
# 
# 输入：S = "a2345678999999999999999", K = 1
# 输出："a"
# 解释：
# 解码后的字符串为 "a" 重复 8301530446056247680 次。第 1 个字母是 "a"。
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= S.length <= 100
# S 只包含小写字母与数字 2 到 9 。
# S 以字母开头。
# 1 <= K <= 10^9
# 解码后的字符串保证少于 2^63 个字母。
# 
# 
#

# @lc code=start
class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        K = K-1
        # 暴力试一下
        nums = [str(i) for i in range(1,10)]
        sub_str = []
        times = []
        pre = 0
        for i in range(len(S)):
            if S[i] in nums:
                # 如果是数字，则拆分
                sub_str.append(S[pre:i])
                times.append(int(S[i]))
                pre = i+1
        if len(times) == 0:
            return S[K]
        # 元素和重复次数都已经记录下来了
        length = 0
        # 计算总长度
        for i in range(len(times)):
            length = (length+len(sub_str[i]))*times[i]
        print(length)
        # 从后向前分解，看最终落在哪个字符串中
        for i in range(len(times)-1,-1,-1):
            temp1 = K % (length//times[i])
            temp2 = length//times[i]-len(sub_str[i])
            if temp1 >= temp2:
                s_idx = temp1-(temp2)
                return sub_str[i][int(s_idx)]
            K = temp1
            length = temp2

        # 直接得出最终字符串，全部直接展开超内存限制
        # s = ''
        # for i in range(len(times)):
        #     # length = (length+len(sub_str[i]))*times[i]
        #     s = (s+sub_str[i])*times[i]
        # return s[K]

# @lc code=end
S = "ixm5xmgo78"
K = 711
solu = Solution()
print(solu.decodeAtIndex(S,K))
