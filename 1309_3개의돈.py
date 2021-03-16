n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)
def solution(n,arr):
    dp=[0,0,0]
    dp[1]=arr[1]
    dp[2]=arr[1]+arr[2]
    for i in range(3,n+1):
        dp.append(max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i],dp[i-1]))
    print(dp[n])

solution(n,arr)