import math
 
def minimum_moves(r, x, y, xx, yy):
    dis = math.sqrt((xx - x)**2 + (yy - y)**2)
    max_mov = 2 * r
    movs = math.ceil(dis / max_mov)
 
    return movs
 
r, x, y, xx, yy = map(int, input().split())
res = minimum_moves(r, x, y, xx, yy)
print(res)
