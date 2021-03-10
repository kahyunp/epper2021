x=input()
def solution(input):
    input=int(input)
    room= (input // 15)+1
    serial = input % 15
    if(serial == 0):
        room-=1
        serial=15
    print(room," ",serial)

solution(x)