def group_by(func, iterable):
    dict={}
    for item in iterable:
        key=func(item)
        if key not in dict:
            dict[key]=[item]
        else:
            dict[key].append(item)
    return dict

if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))