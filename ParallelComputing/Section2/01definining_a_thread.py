from threading import Thread

def myfunction(i):
    print ("function called by thread %i\n"  %i)
    return

threads = []
for i in range(5):
    t = Thread(target=myfunction , args=(i,))
    threads.append(t)
    t.start()
    t.join()

print(threads)