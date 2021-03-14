#회전문 문제
#포인터 두개 사용하기
#pop 하면 end 줄여주기
def solution(arr, start, end):
    	answer=0
	if(arr[start]==arr[end]):
		start+=1
		end-=1
	else:
		while(start < end):
			if (arr[start]<arr[end]):
				arr[start]=arr[start]+arr[start+1]
				arr.pop(start+1)
				end-=1
				answer+=1

			elif (arr[end]<arr[start]):
				arr[end-1]=arr[end]+arr[end-1]
				arr.pop(end)
				end-=1
				answer+=1
			else:
				break
	return answer
			
					
			

n = int(input())
arr = list(map(int,input().split()))

start = int(0);
end = int(n-1);

print(solution(arr, start, end))
