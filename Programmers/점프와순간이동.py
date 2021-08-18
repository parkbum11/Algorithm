# ans = 987654321
# def DFS(batt, dist, glob):
#     global ans
#     if batt > ans or dist > glob:
#         return
#     if dist == glob:
#         if batt < ans:
#             ans = batt
#         # ans = batt
#         return
#     DFS(batt, dist * 2, glob)
#     DFS(batt + 1, dist + 1, glob)
#
# def solution(n):
#     DFS(1, 1, n)
#     print(ans)
#     return ans
# solution(5)

# from collections import deque
# def solution(n):
#     ans = n
#     q = deque()
#     q.append((1, 1))
#     while q:
#         # print(q)
#         batt, dist = q.popleft()
#         if dist == n:
#             if ans > batt: ans = batt
#         if batt >= ans or dist > n: continue
#         q.append((batt, dist * 2))
#         q.append((batt + 1, dist + 1))
#     print(ans)
#     return ans
# solution(5000)

def solution(n):
    ans = 0
    while n != 0:
        print(n)
        if n & 1:
            ans += 1
            n -= 1
        else:
            n //= 2
    print(ans)
    return ans
solution(5000)

def solution(n):
    print(bin(n))
    return bin(n).count('1')
solution(5000)