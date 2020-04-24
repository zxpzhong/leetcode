# 核心：
# 虽然说统计的是横放、竖放所有的方案总数，但是实际上，只需要统计横放后，合理得总数
# 合理：横放后，每一列列连续空位置的数目为偶数就OK

def exam():
    print('123')
exam()
# -------------其他人的代码，自己不想写了，直接帮他优化吧！！！
n = 11
m = 11
if True:
# while True:
    # n行m列
    # n, m = map(int, input().split())    
    # 储存有效状态
    st = [True for i in range(1<<n)]
    # st = 1<<n
    # st = 1<<(n+1) -1
    # st = 0
    # n/m中有一个为0则退出
    if n|m:
        # i = 0 ~ 2^n-1
        for i in range(1<<n):
            cnt = 0
            # j = 0 ~ n-1【遍历这个状态的每一行，即从i-1列是否有东西伸到第i列】
            for j in range(n):
                # 如果状态i的第j位为1，那么当前这个状态下第j行不可能放置方块【即有方块伸到第i列，那么第i列的j行不可能放置方块】
                if (i>>j) & 1:
                    # 如果cnt为奇数，那么该状态不行【任意一个位置进来，那么cnt一定都要为偶数】
                    # 对状态i置false
                    if cnt & 1: st[i] = False
                    # if cnt & 1: st |= 1<<i
                    cnt = 0
                # 否则的话，才可以放置方块
                else: cnt += 1
            # 如果cnt为奇数
            if cnt & 1: st[i] = False
            # if cnt & 1: st |= 1<<i
        # print(st)

        # 初始化dp数组，一共m+1列，每一列2^n-1个状态
        dp = [[0 for i in range(1<<n)] for j in range(m+1)]
        # 第0列有且只能是伸出0个为一种状态【第0列不可能从-1列伸出任何一个方块】
        dp[0][0] = 1
        
        # 状态计算，遍历每一列
        for i in range(1, m+1):
            # 每一个状态
            for j in range(0, 1<<n):
                # 遍历上一列的状态
                for k in range(0, 1<<n):
                    # 上一列的状态j能否转移到当前状态k，并且st是合法的状态
                    if ((j & k) ==0) and st[j|k]:
                    # if ((j & k) ==0) and not st>>(j|k)&1:
                        # 如果能转移且合法，则方法数加上所有可以转移过来的方法
                        dp[i][j] += dp[i-1][k]
        # 最终的答案为最后一列，且伸出0个方块出来【刚好填完最后一列，且不伸出最后一列】
        print(dp[m][0])
    else:
        # break
        pass
