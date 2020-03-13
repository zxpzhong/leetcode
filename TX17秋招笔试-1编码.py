'''题目
假定一种编码的编码范围是a ~ y的25个字母，从1位到4位的编码，如果我们把该编码按字典序排序，形成一个数组如下： a, aa, aaa, aaaa, aaab, aaac, … …, b, ba, baa, baaa, baab, baac … …, yyyw, yyyx, yyyy 其中a的Index为0，aa的Index为1，aaa的Index为2，以此类推。 编写一个函数，输入是任意一个编码，输出这个编码对应的Index.
输入一个待编码的字符串,字符串长度小于等于100.
输出这个编码的index
baca
16331

qqq
271251
'''

import sys
s = sys.stdin.readline().strip()
# print(s)
length = len(s)
# print(length)
candi = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']
ans = 0
for i in range(length):
    temp = [25**j for j in range(4-i)]
    base = sum(temp)
    ans+=candi.index(s[i]) * base
print(ans+length-1)