#הנחה לפי הדוגמא, שכל האיטריבלים באורך זהה

def interleave(*iterables):
    result = []
    for group in zip(*iterables):
        result.extend(group)
    return result

def generator(*iterables):
    for group in zip(*iterables):
        for item in group:
            yield item

if __name__ == "__main__":
    print('interleave:')
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    print('generator:')
    print(list(generator('abc', [1, 2, 3], ('!', '@', '#'))))