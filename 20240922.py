# a,b = map(int,input("").split())
# print(f"{a+b}")

# a,b = map(int,input("").split())
# print(f"{a-b}")


import math

def find_intersections(T, cases):
    results = []
    for i in range(T):
        x1, y1, r1, x2, y2, r2 = cases[i]
        
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        if d == 0 and r1 == r2:
            results.append(-1)  # 무한대
        elif d == r1 + r2 or d == abs(r1 - r2):
            results.append(1)   # 접점이 1개
        elif abs(r1 - r2) < d < (r1 + r2):
            results.append(2)   # 교차점이 2개
        else:
            results.append(0)   # 교차점이 없음
            
    return results


T = int(input())
cases = [tuple(map(int, input().split())) for _ in range(T)]
results = find_intersections(T, cases)

for result in results:
    print(result)

