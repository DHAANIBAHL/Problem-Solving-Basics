num=int(input())
count=0
factors=[]
for i in range(1, num+1):
    if num%i==0:
        count+=1
        factors.append(i)
if count>2:
    print(f'The given number is not prime and its factors are {factors}.')
else:
    print("The given number is prime.")
