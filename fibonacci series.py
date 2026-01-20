def gen_fibonacci(num):
    a=0
    b=1
    series=[0]
    for i in range(1,num):
        a,b=b,a+b
        series.append(a)
    print(series)

num=int(input())
gen_fibonacci(num)


