import math

def solve(a, b, c):
    if ((b * b) - (4 * a * c)) < 0:
        return 'No solutions'
    elif ((b * b) - (4 * a * c)) == 0:
        x1 = ((b * -1) + 0) / (2 * a)
        x2 = ((b * -1) - 0) / (2 * a)
    elif ((b * b) - (4 * a * c)) > 0:
        x1 = ((b * -1) + math.sqrt((b * b) - (4 * a * b))) / (2 * a)
        x2 = ((b * -1) - math.sqrt((b * b) - (4 * a * b))) / (2 * a)
    
    if x1 == x2:
        return f'x = {x1}'
    else:
        return f'x = {x1}, {x2}'