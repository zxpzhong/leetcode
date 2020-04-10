T = int(input().strip())
import functools

@functools.lru_cache()
def DFS(string,ans,k,flag):
    time = 0
    if len(string) == 0:
        if ans == k:
            return 1
        else:
            return 0
    for i in range(1,len(string)+1):
        if flag == 0:
            # -号不能在首位
            time+=DFS(string[i:],ans+int(string[:i]),k,1)
        else:
            time+=DFS(string[i:],ans+int(string[:i]),k,1)
            time+=DFS(string[i:],ans-int(string[:i]),k,1)
    return time
for _ in range(T):
    s,k = list(input().strip().split())
    k = int(k)
    # 字符串s加入任意多的+、-。使结果k
    print(DFS(s,0,k,0))


