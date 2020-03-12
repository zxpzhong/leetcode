'''题目：
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
输出需要删除的字符个数。
abca
abcda
google
1
2
2
'''

'''
解题思路：
  （1）把字符串旋转形成另外一个字符串，称为旋转字符串；
  （2）求原字符串s1与旋转字符串s2中，最长公共子串的长度；
  （3）删除的字符数目 = 原字符串的长度 - 最长公共子串的长度。
需要解决的子问题：
   求两个字符串s1和s2中最长公共子串的长度。
   子问题的求解方式：动态规划
     设 MaxLen(i,j)表示s1左边i个字符与s2左边j个字符的最长公共子串长度，则子问题的解为MaxLen(strlen(s1),strlen(s2));
     MaxLen(i,j)的求解方式为：
       若s1第i个字符与s2第j个字符相匹配，则 return 1+MaxLen(i-1,j-1);
       否则：return max(MaxLen(i-1,j),MaxLen(i,j-1))
    边界条件：
    MaxLen(i,n)=0; for n in 0 to strlen(s2)
    MaxLen(n,j)=0; for n in 0 to strlen(s1)
'''
import sys 
texts = []
# for line in sys.stdin:
    # texts.append(line.split())
texts = [
    'zgtklhfzomzjckwmluvivvcmhjrwkuvcjrxojobpdedpamdshcwwsetfbacvonecrdvugeibglvhxuymjvoryqjwullvzglqazxrdmczyvbgakjagttrezmvrlptiwoqkrtxuroeqmryzsgokopxxdpbejmtwvpnaqrgqladdszhdwxfckmewhdvihgvacueqhvwvjxoitlpfrckxkuksaqzjpwgoldyhugsacflcdqhifldoaphgdbhaciixouavqxwlghadmfortqacbffqzocinvuqpjthgekunjsstukeiffjipzzabkuiueqnjgkuiojwbjzfynafnlcaryygqjfixaoeowhkxkbsnpsvnbxuywfxbnuoemxynbtgkqtjvzqikbafjnpbeirxxrohhnjqrbqqzercqcrcswojyylunuevtdhamlkzqnjrzibwckbkiygysuaxpjrgjmurrohkhvjpmwmmtpcszpihcntyivrjplhyrqftghglkvqeidyhtmrlcljngeyaefxnywpfsualufjwnffyqnpitgkkyrbwccqggycrvoocbwsdbftkigrkcbojuwwctknzzmvhbhbfzrqwzllulbabztqnznkqdyoqnrxhwavqhzyzvmmmphzxbikpharseywpfsqyybkynwbdrgfsaxduxojcdqcjuaywzbvdjgjqtoffasiuhvxcaockebkuxpiomqmtvsqhnyxfjceqevqvnapbk',
'abcda',
'google']
for text in texts:
    # 动态规划
    dp = [[0 for i in range(len(text))] for i in range(len(text))]
    length = len(text)
    for i in range(length):
        # 首先填充第一行
        if not text[i] == text[length-1]:
            continue
        else:
            for t in range(i,length): dp[0][t] = 1
            break
    for i in range(length):
        # 第一列
        if not text[length-1-i] == text[0]:
            continue
        else:
            for t in range(i,length): dp[t][0] = 1
            break
    # 初始化完毕
    inv_text = text[::-1]
    for i in range(1,length):
        for j in range(1,length):
            if text[j] == inv_text[i]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    print(length-dp[-1][-1])


