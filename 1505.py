def solution(input):
    text_arr=list(input)
    print(text_arr)
    n=len(text_arr)
    cnt=0
    answer=''
    a=ord("A")
    if(text_arr[0]=='1'):
        answer='1'

    for i in range(n-1):
        if(text_arr[i] != text_arr[i+1]):
            answer+=chr(a+cnt)
            cnt=0
        else:
            cnt+=1
    answer+=chr(a+cnt)
    print(answer)
    
x=input()
solution(x)

