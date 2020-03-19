'''
https://www.acwing.com/problem/content/604/
给定一个仅包含0或1的字符串，现在可以对其进行一种操作：

当有两个相邻的字符其中有一个是0另外一个是1的时候，可以消除掉这两个字符。

这样的操作可以一直进行下去直到找不到相邻的0和1为止。

问这个字符串经历了操作以后的最短长度。

输入格式
第一行包含一个整数 n，表示字符串的初始长度。

第二行为所给字符串。

输出格式
输出共一行，包含一个整数，表示问题的解。

数据范围
1≤n≤2∗105
输入样例1：
4
1100
输出样例1：
0
输入样例2：
5
01010
输出样例2：
1
'''

import sys
n = list(map(int,sys.stdin.readline().strip().split()))[0]
s = sys.stdin.readline().strip()

# # 和找括号是一个意思，用堆做？但是01不是固定的
# list1 = []
# list0 = []

# while True:
#     pt = 0
#     while pt < len(s)-1:
#         if (s[pt] == '0' and s[pt+1] == '1') or (s[pt] == '1' and s[pt+1] == '0'):
#             s = s[:pt]+s[pt+1+1:]
#             break
#         pt+=1
#     if pt == len(s):
#         break
# print(len(s))
from collections import Counter
temp = Counter(s)
print(abs(temp['1']-temp['0']))
