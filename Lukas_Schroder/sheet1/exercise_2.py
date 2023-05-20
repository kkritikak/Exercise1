
from random import uniform
from threading import Thread

num_threads = 64
iter=int(1e5)
results = [None] * num_threads

def rand ():
    random = uniform(-1,1)
    return random if (random > -1 and random < 1) else rand()

def monte_carlo_pi (thidx : int, iterations : int, result : float):
    hits = 0
    for _ in range(iterations):
        r = (rand(), rand())
        if ((r[0]**2 + r[1]**2) <= 1): hits += 1
        results[thidx] = 4*hits/iterations
    return 

if __name__ == "__main__":
    threads = [Thread(target=monte_carlo_pi,
        args=[i, iter, results] ) for i in range(num_threads)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    pi = sum(results)/num_threads

    print("PI="+str(pi))
        