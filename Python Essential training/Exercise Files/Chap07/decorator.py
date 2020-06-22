import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f() #Aqui es donde se ejecuta realmente la función.
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper


@elapsed_time #llama al decorate, pasando en f la propia función big_sum
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')

def main():
    big_sum()

if __name__ == '__main__': main()
