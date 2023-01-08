import threading
import time
import queue

def task(q, n, dt, reps):
    print(f'{n} starts')
    for k in range(reps):
        time.sleep(dt)
        q.put((time.time(), n))
    print(f'{n} finishes')

def queuetask(q, n):
    for k in range(n):
        # skriver ut första numret i kön, väntar upp till timeout s om kön är tom
        print(q.get(timeout = 5), time.time())

q = queue.Queue()

thread1 = threading.Thread(target = task, args = (q, 1, 2, 9))
thread2 = threading.Thread(target = task, args = (q, 2, 3, 6))

thread1.start()
thread2.start()
# med join, så väntar main tills tråden är färdig, utan så fortsätter den.
#thread1.join()
#thread2.join()
print('Nu kör main!')

thread3 = threading.Thread(target = queuetask, args = (q, 15))
thread3.start()
