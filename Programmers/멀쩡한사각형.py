# 집가서 푼다
import math
def solution(w,h):
    return w * h - (w + h - math.gcd(w, h))

solution(8, 12)