arr=list(map(int,input().split()))
isEven=[]
count=0

for i in arr:
    if i%2==0:
        count+=1
        isEven.append(i)
print(f'There are {count} even numbers and they are {isEven}')