def integer_checker(a, b, c):
    if a > 0 and b > 0 and c < 0 or a > 0 and c > 0 and b < 0 or b > 0 and c > 0 and a < 0 :
        return True
    else:
        return False

print(integer_checker(-12, -6, 0))
