# Joseph Ernest, 2016/11/12

import sys,time
from . import daemon

class testdaemon(daemon.Daemon):
    def run(self):
        self.i = 0
        with open('test1.txt', 'w') as f:
            f.write(str(self.i))
        while True:
            self.i += 1
            time.sleep(1)

    def quit(self):
        with open('test2.txt', 'w') as f:
            f.write(str(self.i))

daemon = testdaemon()

if 'start' == sys.argv[1]: 
    daemon.start()
elif 'stop' == sys.argv[1]: 
    daemon.stop()
elif 'restart' == sys.argv[1]: 
    daemon.restart()