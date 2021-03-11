def solution(input, price):
    change=input-price
    type=0
    cnt=0
    type_arr=[50000,10000,5000,1000,500,100,50,10]
    for i in type_arr:
        if (change // i):
            type+=1
            cnt+= change // i
            change %= i
            
        else:
            pass
    print("%d %d"%(type,cnt))

solution(10000,8240)

