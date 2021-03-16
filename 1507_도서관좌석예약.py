s=[0,6,3,1,1,2]
e=[3,7,10,5,9,8]

def solution(s,e):
    arr=[]
    e1=-1
    e2=-1
    answer=0
    for i in range(len(s)):
        pair=[e[i],s[i]]
        arr.append(pair)
    arr=sorted(arr)
    for i in arr:
        pair=i
        if(e1 <=pair[1]):
            e1=pair[0]
            answer+=1
        elif (e2 <= pair[1]):
            e2=e1
            e1=pair[0]
            answer+=1
    print(answer)



solution(s,e)