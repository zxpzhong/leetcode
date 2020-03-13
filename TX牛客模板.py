'''题目
    
'''

import sys
s = sys.stdin.readline().strip()

n = list(map(int,sys.stdin.readline().strip().split()))[0]

texts = []
for line in sys.stdin:
    texts.append(line.split())