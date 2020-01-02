from multiprocessing import Process
import time
class MyNewProcess(Process):
    """docstring for MyNewProcess"""
    def __init__(self):
        super(MyNewProcess, self).__init__()

    def run(self):
        while True:
            print("-----1-----")
            time.sleep(1)
        pass

p = MyNewProcess()
p.run()
