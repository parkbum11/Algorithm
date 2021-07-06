import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())
result = N
for i in arr:
    if (i - B) > 0:
        if (i - B) % C:
            result += (i - B) // C + 1
        else:
            result += (i - B) // C
print(result)

# best

# N=int(input())
# A=list(map(int, input().split()))
# B,C= map(int, input().split())
# su=N
# for i in range(N):
#     A[i]-=B+1
#     if A[i]>=0:
#         tem= (A[i])//C+1
#         su+=tem
# print(su)

