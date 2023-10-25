from multiprocessing import Pool
import sys
import time

def f(x):
    time.sleep(5)
    return x

def waitingAnimation(n):
    n = n%3+1
    dots = n*'.'+(3-n)*' '
    sys.stdout.write('\r Waiting '+ dots)
    sys.stdout.flush()
    time.sleep(0.5)
    return n

if __name__ == '__main__':
    print('\n Starting function')
    with Pool(processes=1) as pool:
        res = pool.apply_async(f, (1,))
        waiting, n = True, 0
        while waiting:
            try:
                waiting = not res.successful()
                data = res.get()
            except AssertionError:
                n = waitingAnimation(n)
        sys.stdout.write('\r Function complete\n')