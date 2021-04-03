# https://youtu.be/FLp2SCNyhhg
import memory_profiler

@memory_profiler.profile
def big_array():
    x = [1] * (10**5)
    y = [2] * (10**7)
    del y
    return x

if __name__== '__main__':
    big_array()
