num=int(input())
rev_dig=0

while num>0:
    rev_dig=(rev_dig*10) + (num%10)
    num=num//10
print(rev_dig)


