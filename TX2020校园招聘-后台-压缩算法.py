# import sys 
# s = sys.stdin.readline().strip()
# # s = '[14|FSFVSW]FSFA[3|SDFSF[8|SFSF]FSF]'
# while True:
#     # 由内到外拆解
#     pt1 = 0
#     pt2 = 1
#     length = len(s)
#     i = 0
#     while i < length:
#         if s[i] == '[':
#             pt1 = i
#         elif s[i] == ']':
#             pt2 = i
#             break
#         i+=1
#     if i == length:
#         break
#     # 已经找到最内层一组[]，进行解码
#     temp_s = s[pt1+1:pt2]
#     split_idx = temp_s.index('|')
#     # 解码插入字符串
#     ins_s = temp_s[split_idx+1:]*int(temp_s[:split_idx])
#     s = s[:pt1]+ins_s+s[pt2+1:]
# print(s)


# 换用栈
import sys 
s = sys.stdin.readline().strip()
stack = []
# 由内到外拆解
i = 0
length = len(s)
while i < length:
    if s[i] == '[':
        stack.append(i)
    if s[i] == ']':
        if i == len(s):
            break
        pt1 = stack.pop()
        pt2 = i
        # 已经找到最内层一组[]，进行解码
        temp_s = s[pt1+1:pt2]
        split_idx = temp_s.index('|')
        # 解码插入字符串
        ins_s = temp_s[split_idx+1:]*int(temp_s[:split_idx])
        s = s[:pt1]+ins_s+s[pt2+1:]
        # 解码后i的位置
        i = pt1+len(ins_s)
        length = len(s)
        continue
    i+=1
print(s)