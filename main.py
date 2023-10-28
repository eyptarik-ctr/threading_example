import threading
import time
sonuç = 0
def threadFunction_1():
    for i in range(1,5):
        time.sleep(1)
        print(f"hello {i}")

def threadingUnction_2():
    for x in range(5):
        time.sleep(1)

        print(f"printed {x}")
def threading_func3():
    for y in range(5):
        time.sleep(1)
        print(f"hello {y}")

thread1 = threading.Thread(target=threadFunction_1)
thread2 = threading.Thread(target=threadingUnction_2)
thread3 = threading.Thread(target=threading_func3)
def hız_ölçer():
    global sonuç
    bt = time.time()
    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()
    st = time.time()
    sonuç = st-bt

hız_ölçer()

timeb = time.time()
threadFunction_1()
threading_func3()
threadingUnction_2()
times = time.time()
print(f"normal execute : {times - timeb}")
print(f"thrad çoklu işlemler le bir kaç fonksiyonu aynı anda çalıştırın :{sonuç}")



