import time


def display_time(func):
    def wrapper(*args):
        t1 = time.perf_counter()
        result = func(*args)
        t2 = time.perf_counter()
        print("Total time: {:} ms".format((t2 - t1) * 1000))
        return result

    return wrapper


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            return True


@display_time
def waste_time(num):
    for i in range(num * 10):
        pass


@display_time
def count_prime_nums(num):
    count = 0
    for i in range(2, num + 1):
        if is_prime(i):
            count = count + 1
    return count


if __name__ == '__main__':
    num = count_prime_nums(500000)
    print(num)
    waste_time(100000)
