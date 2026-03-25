import time

def timer(f,*args):
    start=time.time()
    f(*args)
    end=time.time()
    print(f'{f.__name__} took {end-start:.4f} seconds')

if __name__ == "__main__":
    timer(print, "Hello")
    timer(zip, [1, 2, 3], [4, 5, 6])