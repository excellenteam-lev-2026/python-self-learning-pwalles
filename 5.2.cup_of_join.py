def join(*lsts, sep='-'):
    lst=[]
    if len(lsts)==0:
        return None
    for i in lsts:
        lst+=i
        lst+=sep
    lst.pop()
    return lst

if __name__ == "__main__":
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
    print(join([1, 2], [8], [9, 5, 6]))
    print(join([1]))
    print(join())