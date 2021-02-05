
def qs(s,left,right):
    if left>=right:
        return
    bot = left
    top = right
    pivot = s[bot]
    while(bot<top):
        while bot<top and s[bot]<pivot:
            top-=1
        s[bot]=s[top]
        while bot<top and s[top]>=pivot:
            bot+=1
        s[top]=s[bot]
    s[top]=pivot
    qs(s,bot,left-1)
    qs(s,left+1,top)

def solution(s,k):
    qs(s,0,len(s)-1)
    return s[-k]


s = [3,2,1,4,5]
print(solution(s,2))