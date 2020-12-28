def nestedBone(z):
    if z == []:
        return z
    if isinstance(z[0], list):
        return nestedBone(z[0]) + nestedBone(z[1:])
    return z[:1] + nestedBone(z[1:])

def garbageList(x):
    if type(x) == list:
        x = nestedBone(x)
        if len(x) == 1:
            return x.pop()
        else:
            return x.pop() + garbageList(x)
    else:
       return False