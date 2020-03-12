'''题目
小Q最近遇到了一个难题：把一个字符串的大写字母放到字符串的后面，各个字符的相对位置不变，且不能申请额外的空间。
你能帮帮小Q吗？
输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.
对于每组数据，输出移位后的字符串。
AkleBiCeilD
kleieilABCD
'''
import sys 
# for line in sys.stdin:
    # s = line.split()
s = 'hxKLAGLLzPyTxsFsrUnnSKQBHdQQrOyaEYJRgiJbHIDXFcQkFmIhPNKIBfHxXDBdKAvgZiBLVwnlxJAHmttsSJkZhSmQneNVoKoIYZRjPqsrFFaaqZbyNyeRjVKVFrCGdfycidTqbyQcpAtdRGzzBAaKoqybWMOyhrCQdwcRwQQpQavTnAbjriVwxJOrTYJVGYSWzKYeNAGqBzkJLucabNYvyVFxAGKLfqHXNttaqZfncEdTroGMzZnDbvZBBaRbJvuYIvlWrKaaGrvtyxrsCUOqxdwCrmVEeDrLKZKFJVRmrLsmbmOGUJyfdZIrFhuSwJQGRTYMLxKQNMaCavatlQIRZmFQvyWgQTVENxUcPKQCaUQbjyfaNuwoNdTBNldgrtPUcQodqsuJOdDpUczJWCZaasDdEYJkvituMHrCmZQSlRjIefVisatIUtfxBeKnHPyvWUKzRliFsYWgeXogiEgXDbfxAybwFuqFyEvjfIHEPDPKqEiGUtZhdDIDBGKpvBFyqHeEEhAToAbqHEpIdIhIGBtWjGHiQRctZxQQYkfFoWUbqZyIcjRPQBilHrnqNBzFmoRUYCSrGkawJCcOrMceegISpIpSGVjbngWVMTYtGoAlQFPFyOFAxndJZNfKDTwFIxisKTjyjchidXpYgLfoBOLriuIAHmAbQwoHBgbdUYBHlDQGZJASsHszOEPthLVnYbNqWegmONexfdsTVYHgtDmlyugefOBsqmgNDBoxkkhVHfvrYooVOyxDJQJLjYSngksbTopoPJFsKQzHePLukXyYTYCeW'
s_list = [s[i] for i in range(len(s))]
pt1 = 0
pt2 = 1
while pt2 < len(s_list):
    if s_list[pt1].isupper() and not s_list[pt2].isupper():
        # pt1-pt2为大写，pt2为小写
        temp = s_list[pt2]
        for i in range(pt2-pt1):
            s_list[pt2-i] = s_list[pt2-i-1]
        s_list[pt1] = temp
    elif s_list[pt1].isupper() and s_list[pt2].isupper():
        pt2+=1
    else:
        # 否则，pt1,2都往前跑
        pt1+=1
        pt2+=1
a = ''
for item in s_list:
    a+=item
print(a)