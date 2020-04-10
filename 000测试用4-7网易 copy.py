T = int(input().strip())

rows = [0,0,-1,1,1,1,-1,-1,-1]
cols = [-1,1,0,0,-1,1,-1,1]

# DFS
def DFS(x,y,laser_,count,ex,ey,seen):
    ans = m*n+1
    if x == ex and y == ey:
        return count
    for i in range(8):
        if not(0<=x+rows[i]<n and 0<=y+cols[i]<m):
            continue
        if laser_[x+rows[i]][y+cols[i]] == 3:
            continue
        if seen[x+rows[i]][y+cols[i]] == 1:
            continue
        # 两边是否有激光器
        # if laser_
        seen[x+rows[i]][y+cols[i]] = 1
        # 这一步两段是否有激光器，还跟方向有关！！！
        # 从x,y 到 x+rows[i] y+cols[i]
        if laser_[x+rows[i]][y+cols[i]] == 1 or laser_[x+rows[i]][y+cols[i]] == 2:
            ans = min(ans,DFS(x+rows[i],y+rows[i],laser_,count+1,ex,ey,seen))
        else:
            ans = min(ans,DFS(x+rows[i],y+rows[i],laser_,count,ex,ey,seen))
        seen[x+rows[i]][y+cols[i]] = 0
    return ans

for _ in range(T):
    # 读取地图信息
    n,m = list(map(int,input().strip().split()))
    sx,sy,ex,ey = list(map(int,input().strip().split()))
    seen = [[0]*m for _ in range(n)]
    sx-=1
    sy-=1
    ex-=1
    ey-=1
    k = int(input().strip())
    lasers = []
    things = []
    for _ in range(k):
        x,y,op = input().strip().split()
        x = int(x)-1
        y = int(y)-1
        if op == 'B':
            things.append([x,y])
        else:
            lasers.append([x,y,op])
    
    # 八邻域可走，激光遇到障碍物和激光器停止
    # 走的路径中相邻两个格子最多只能有一个有激光【沿路径垂直方向】
    # 路径最少有几个被激光照射
    
    # 激光存在的矩阵
    laser_ = [[0]*m for _ in range(n)]
    for item in (things):
        laser_[item[0]][item[1]] = 3
    for item in lasers:
        x,y = item[0],item[1]
        laser_[x][y] = 2
    for item in lasers:
        x,y = item[0],item[1]
        dir = item[2]
        if dir == 'u':
            pt = x-1
            while pt >-1 and laser_[pt][y] <= 1:
                laser_[pt][y] = 1
                pt-=1
        elif dir == 'd':
            pt = x+1
            while pt <n and laser_[pt][y] <=1:
                laser_[pt][y] = 1
                pt+=1
        elif dir == 'l':
            pt = y-1
            while pt >-1 and laser_[x][pt] <=1:
                laser_[x][pt] = 1
                pt-=1
        elif dir == 'r':
            pt = y+1
            while pt <n and laser_[x][pt] <=1:
                laser_[x][pt] = 1
                pt+=1
    seen[sx][sy] = 1
    temp = DFS(sx,sy,laser_,0,ex,ey,seen)
    if temp == m*n+1:
        print(-1)
    else:
        print(temp)