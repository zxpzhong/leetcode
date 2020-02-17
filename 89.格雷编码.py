#
# @lc app=leetcode.cn id=89 lang=python
#
# [89] 格雷编码
#
# https://leetcode-cn.com/problems/gray-code/description/
#
# algorithms
# Medium (66.02%)
# Likes:    123
# Dislikes: 0
# Total Accepted:    17.7K
# Total Submissions: 26.2K
# Testcase Example:  '2'
#
# 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
# 
# 给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。
# 
# 示例 1:
# 
# 输入: 2
# 输出: [0,1,3,2]
# 解释:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# 
# 对于给定的 n，其格雷编码序列并不唯一。
# 例如，[0,2,3,1] 也是一个有效的格雷编码序列。
# 
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
# 
# 示例 2:
# 
# 输入: 0
# 输出: [0]
# 解释: 我们定义格雷编码序列必须以 0 开头。
# 给定编码总位数为 n 的格雷编码序列，其长度为 2^n。当 n = 0 时，长度为 2^0 = 1。
# 因此，当 n = 0 时，其格雷编码序列为 [0]。
# 
# 
#

# @lc code=start
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 列出所有的序列
        if n == 0:
            return [0]
        self.n = n
        self.length = pow(2,n)
        self.candi = []
        ans = '0'*n
        self.candi.append(ans)
        self.add_1(ans)
        print(self.candi)
        # 二进制转
        for i in range(self.length):
            self.candi[i] = int(self.candi[i],2)
        return self.candi
        
    def add_1(self,cur_str):
        if len(self.candi) == self.length:
            return True
        for i in range(self.n):
            # 每次变1位
            temp = cur_str[:i]+str(1-int(cur_str[i]))+cur_str[i+1:]
            if not temp in self.candi:
                self.candi.append(temp)
                if self.add_1(temp) == True:
                    return True
        return False
        
# @lc code=end
solu = Solution()
print(solu.grayCode(2))
