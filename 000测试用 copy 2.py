n = int(input())
a = list(map(int, input().split()))

list_ = []
for i in range(len(a)):
    for j in range(i, len(a)):
        list_.append(min(a[i: j+1])^max(a[i: j+1]))

result = list_[0]
for i in range(1, len(list_)):
    result = result^ list_[i]
print(result)

