arr=list(map(int,input().split()))
max=0

l=len(arr)

for i in range(l-1):
    if arr[i]>max:
        max=arr[i]
print(max)