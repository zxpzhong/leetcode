'''
[气球游戏]小Q在进行射击气球的游
戏，如果小Q在连续T枪中打爆了所有颜
色的气球，将得到一只QQ公仔作为奖
励。(每种 颜色的气球至少被打爆一
只)。这个游戏中有m种不同颜色的气
球，编号1到m。小Q一共有n发子弹，
然后连续开了n枪。小Q想知道在这n枪
中，打爆所有颜色的气球最少用了连续
几枪?
输入描述:
第一行两个空格间隔的整数数n，m。
n<=1000000 m<=2000
第二行一-共n个空格间隔的整数，分别表
示每一枪打中的气球的颜色,0表示没打
中任何颜色的气球。
输出描述:
一个整数表示小Q打爆所有颜色气球用
的最少枪数。如果小Q无法在这n枪打爆
所有颜色的气球，则输出-1
示例
输入:
12 5
2 531 32410543
输出:
6
'''

#coding=utf-8
import sys 
text = []
for line in sys.stdin:
    text.append(line.split())
n = int(text[0][0])
m = int(text[0][1])
candidate = text[1]
# 转换为int方便后面处理
candidate = [int(candidate[i]) for i in range(n)]
# print(candidate)
# 构建候选序列 
dp = [-1 for i in range(m)]
min_len = 1000001
for i in range(n):
    # 如果遇到未命中,直接清空
    if candidate[i] == 0:
        dp = [-1 for i in range(m)]
        continue
    # 记录当前打爆气球的索引
    dp[(candidate[i])-1] = i
    # 判断是否包含了打爆了所有气球
    if not -1 in dp:
        # 取出最小长度
        min_len = min((max(dp) - min(dp)),min_len)
    # print(dp)
# print('-------')
if min_len == 1000001:
    # 未找到子列
    print(-1)
else:
    print(min_len+1)
# print('Hello,World!')