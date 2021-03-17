k,n=map(int,input().split())

def solution(k,n):
    word=[]
    quiz=[]
    dic={}
    for i in range (k):
        wrd=input()
        word.append(wrd)
    for i in range(n):
        quiz.append(input())
        
    word=sorted(word)
    for i in word:
        dic[i]=0
       
    for j in quiz:
        cnt=0
        maybe=[]
        freq=[]
        ans=''

        for p in word:  
            if(j==p[0]):
                maybe.append(p)
                cnt+=1
        if(cnt==1):
            dic[maybe[0]]+=1
            ans=maybe[0]
        else:
            for i in maybe:
                freq.append(int(dic[i]))
            ans=maybe[freq.index(min(freq))]
            dic[ans]+=1
        print(ans)

solution(k,n)
