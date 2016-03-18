def majority(a):
    if len(a) == 0:
        return None
    if len(a) == 1:
        return a[0]
    half = len(a) // 2
    left = majority(a[0:half])
    right = majority(a[half:])
    if left == right:
        return left
    if a.count(left) > half:
        return left
    if a.count(right) > half:
        return right
    return None
