'''
牛家村的货币是-种很神奇的连续货币。
他们货币的最大面额是n,并且-共有面额为1,面额为2... 面额为n, n种面额的货币。
牛牛每次购买商品都会带上所有面额的货币看，支付时会选择给出硬币数量最小的方案。
现在告诉你牛牛将要购买的商品的价格，你能算出牛牛支付的硬币数量吗? (假设牛牛 每种面额的货币都拥有无限个。)
输入描述:
第一行两个整数n，m。表示货币的最大面额和商品的价格。
1<=n<=100000，1<=m<=000000000
输出描述:
一个整数表示牛牛支付的硬币数量。
示例
1 //输入:
2
57
3 // 输出:
4

https://www.acwing.com/problem/content/569/
'''


import sys
n = list(map(int,sys.stdin.readline().strip().split()))
n,m = n[0],n[1]
# n为最大面额，m为商品价格
# 每种货币拥有无限个！！！
# 贪心算法：大面额的永远有最多个
ans = m//n
print(ans if m%n == 0 else ans+1)