x=int(input())
list=[]
for i in range(x):
    list.append(int(input()))
list=sorted(list)

#원소개수가 1일때 고려
if(x==1):
    print(x)

#원소 개수가 1보다 클 때
else:
    for i in range(x-1):
        avg=(list[0]+list[1])/2
        list.pop(0)
        list.pop(0)
        list.insert(0,avg)
    #파이썬 소수점 6자리까지
    print(f'%.6f' %avg)
