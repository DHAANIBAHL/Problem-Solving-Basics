arr=list(map(int,input().split()))
min=arr[0]

l=len(arr)

for i in range(l-1):
    if arr[i]<min:
        min=arr[i]
print(min)