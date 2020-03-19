'''
小Q和牛妹参加一个剪刀石头布的游戏，游戏用卡片来玩，每张卡片是剪刀，石头，布中的-种，每种类型的卡片有无限个。牛妹从中选了n张卡片排
成一排，正面朝下，小Q也会选择n张卡片排成一排， 然后小Q和牛妹的卡片会依次进行比对，第一张对第一-张，第二张对第二张..
如果小Q赢，小Q会得到一份，现在已知牛妹的每一张牌 以及小Q的最终得分，请问小Q有多少种选择卡片的方案(多少不同的排列)
输入描述
第一行输入两个数n，s (1<=n<=2000， 0<=s<=2000)
第二行输入n个整数表示牛妹的每张卡片，每个数在(0, 2)之间，0代表石头，1代表布，2代表剪刀。
输出描述
输出一个整数，对le9+7取模
示例
输入
132
2012
输出
1| 6
'''
import sys
# n:卡片数  s：得分
n,s = list(map(int,sys.stdin.readline().strip().split()))
# 牛妹卡片
card = list(map(int,sys.stdin.readline().strip().split()))
# n轮中，赢得s轮，也就是从card中挑出s个赢，剩下输的每一个有两个选择

import math
# print(int((math.factorial(n)/(math.factorial(s)*math.factorial(n-s)))*(2**(n-s)))%(10**9+7))
temp = 1
for i in range(n-s+1,n+1):
    temp*=i
print(int((temp/(math.factorial(s)))*(2**(n-s)))%(10**9+7))

