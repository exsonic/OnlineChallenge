from multiprocessing import Process, Queue
import os, math

def producer(q, proc_num):
    for i in range(10):
        q.put(i)

    for i in range(proc_num):
        q.put(None)

def f(q):
    pid = str(os.getpid())
    print(pid + 'start')
    while True:
        num = q.get()
        if num is None:
            print(pid + 'stop')
            break

        for i in range(num):
            a = math.sqrt(i ** 10)
            print(a)

def run_multi_proc(proc_num):
    proc_list = []
    q = Queue()
    producer_proc = Process(target=producer, args=(q, proc_num,))
    producer_proc.start()

    for i in range(10):
        p = Process(target=f, args=(q,))
        p.start()

    for proc in proc_list:
        proc.join()

    producer_proc.join()

if __name__ == '__main__':
    run_multi_proc(10)
