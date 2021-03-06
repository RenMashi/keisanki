from threading import Thread,Semaphore

def my_function1():
  with semaphore:
    for i in range(10000):
      print("123")
      print("456")
      print("789")

def my_function2():
  with semaphore:
    for i in range(10000):
      print("abc")
      print("def")
      print("ghi")

def my_function3():
  with semaphore:
    for i in range(10000):
      print("ABC")
      print("DEF")
      print("GHI")

if __name__ == "__main__":
  semaphore = Semaphore(1)
  t1 = Thread(target = my_function1)
  t2 = Thread(target = my_function2)
  t3 = Thread(target = my_function3)
  t1.start()
  t2.start()
  t3.start()
  t1.join()
  t2.join()
  t3.join()
