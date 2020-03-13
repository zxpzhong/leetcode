'''题目
在一组数的编码中，若任意两个相邻的代码只有一位二进制数不同， 则称这种编码为格雷码(Gray Code)，请编写一个函数，使用递归的方法生成N位的格雷码。

给定一个整数n，请返回n位的格雷码，顺序为从0开始。

测试样例：
1
返回：["0","1"]
'''


# 太屌了这题，格雷码两种递归方法！！！！
'''
第一种解法，为什么要反向不理解
    //递归
 
    //递归的思路是n位gray码是由n-1位gray码生成，举个例子简单一些：
 
    //比如求n=3的gray码，首先知道n=2的gray码是(00,01,11,10)
 
    //那么n=3的gray码其实就是对n=2的gray码首位添加0或1生成的，添加0后变成(000,001,011,010)
 
    //添加1后需要顺序**反向**就变成(110,111,101,100)
 
    //组合在一起就是(000,001,011,010,110,111,101,100)


第二种解法
//方法二：利用公式G(n) =  n XOR (n/2)，求得gray码的十进制之后再转换成二进制字符串
'''



# 递归解法




#--------------下面是我的弱智暴力解法，n=8时就很耗时了
# -*- coding:utf-8 -*-

# class GrayCode:
#     def gene_next(self,s):
#         if len(s[0]) == self.n:
#             return s
#         new_s = []
#         for i in range(len(s)):
#             new_s.append(s[i]+'0')
#             new_s.append(s[i]+'1')
#         return self.gene_next(new_s)
#     def isOK(self,str1,str2):
#         # count = 0
#         # for i in range(len(str1)):
#         #     if not str2[i] == str1[i]:
#         #         count+=1
#         #         if count >= 2:
#         #             return False
#         if int(str1,2) ^ int(str2,2) in self.candi:
#             return True
#         else:
#             return False
#     def getGray(self, n):
#         self.candi = [2**i for i in range(n)]
#         self.n = n
#         start = ['0','1']
#         ans = self.gene_next(start)
#         # 对格雷码进行排序
#         new_ans = []
#         new_ans.append(ans[0])
#         ans.pop(0)
#         while ans:
#             for i in range(len(ans)):
#                 if self.isOK(new_ans[-1],ans[i]):
#                     # 如果满足要求
#                     new_ans.append(ans[i])
#                     ans.pop(i)
#                     break
#         return new_ans


solu = GrayCode()
print(solu.getGray(8))