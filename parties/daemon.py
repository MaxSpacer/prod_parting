import sys
import os
import time
import atexit
import logging
from signal import signal, SIGTERM
# from django.conf import settings


CHARMAP_LOWERCASE = {4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k',
                     15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v',
                     26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7',
                     37: '8', 38: '9', 39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';',
                     52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'}
CHARMAP_UPPERCASE = {4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K',
                     15: 'L', 16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V',
                     26: 'W', 27: 'X', 28: 'Y', 29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&',
                     37: '*', 38: '(', 39: ')', 44: ' ', 45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':', 52: '"',
                     53: '~', 54: '<', 55: '>', 56: '?'}
CR_CHAR = 40
SHIFT_CHAR = 2
ERROR_CHARACTER = '?'


class BarcodeReader:
    def __init__(self, device_path="/dev/hidraw1"):
        self.device_path = device_path
        self.f = open(self.device_path, "rb")

    def read_barcode(self):
        barcode_string_output = ''
        # barcode can have a 'shift' character; this switches the character set
        # from the lower to upper case variant for the next character only.
        CHARMAP = CHARMAP_LOWERCASE
        while True:
            # step through returned character codes, ignore zeroes
            for char_code in [element for element in self.f.read(8) if element > 0]:
                if char_code == CR_CHAR:
                    # all barcodes end with a carriage return
                    self.f.close()
                    return barcode_string_output
                if char_code == SHIFT_CHAR:
                    # use uppercase character set next time
                    CHARMAP = CHARMAP_UPPERCASE
                else:
                    # if the charcode isn't recognized, use ?
                    barcode_string_output += CHARMAP.get(char_code, ERROR_CHARACTER)
                    # reset to lowercase character map
                    CHARMAP = CHARMAP_LOWERCASE



def barcode_reader(device_path="/dev/hidraw1"):
    reader = BarcodeReader(device_path)
    return reader.read_barcode()


class Daemon:
    """
    A generic daemon class.

    Usage: subclass the Daemon class and override the run() method
    """

    def __init__(self, pidfile='/webapps/prod_parting/run/_scan_daemon.pid', stdin='/webapps/prod_parting/logs/scan_daemon.log', stdout='/webapps/prod_parting/logs/scan_daemon.log', stderr='/webapps/prod_parting/logs/scan_daemon.log'):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.pidfile = pidfile

    def daemonize(self):
        """
        do the UNIX double-fork magic, see Stevens' "Advanced
        Programming in the UNIX Environment" for details (ISBN 0201563177)
        http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
        """
        try:
            pid = os.fork()
            if pid > 0:
                # exit first parent
                sys.exit(0)
        except OSError as e:
            sys.stderr.write("fork #1 failed: %d (%s)\n" %
                             (e.errno, e.strerror))
            sys.exit(1)

        # decouple from parent environment
        os.setsid()
        os.umask(0)

        # do second fork
        try:
            pid = os.fork()
            if pid > 0:
                # exit from second parent
                sys.exit(0)
        except OSError as e:
            sys.stderr.write("fork #2 failed: %d (%s)\n" %
                             (e.errno, e.strerror))
            sys.exit(1)

        # redirect standard file descriptors
        sys.stdout.flush()
        sys.stderr.flush()
        si = open(os.devnull, 'r')
        so = open(os.devnull, 'a+')
        se = open(os.devnull, 'a+')
        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(so.fileno(), sys.stdout.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        atexit.register(self.onstop)
        signal(SIGTERM, lambda signum, stack_frame: exit())

        # write pidfile
        pid = str(os.getpid())
        open(self.pidfile, 'w+').write("%s\n" % pid)

    def onstop(self):
        self.quit()
        os.remove(self.pidfile)

    def start(self, path=None):
        """
        Start the daemon
        """
        # Check for a pidfile to see if the daemon already runs
        # sys.stderr.write('Start the daemon\n')
        try:
            sys.stderr.write('Try starting the daemon\n')
            pf = open(self.pidfile, 'r')
            pid = int(pf.read().strip())          
            pf.close()
            sys.stderr.write('Daemon is started \n')
        except IOError:
            pid = None

        if pid:
            message = "pidfile %s already exist. Daemon already running?\n"
            sys.stderr.write(message % self.pidfile)
            sys.exit(1)

        # Start the daemon
        self.daemonize()
        self.run(path)

    def stop(self):
        """
        Stop the daemon
        """
        # Get the pid from the pidfile
        try:
            pf = open(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
            sys.stderr.write('Stop the daemon\n')
        except IOError:
            pid = None

        if not pid:
            message = "pidfile %s does not exist. Daemon not running?\n"
            sys.stderr.write(message % self.pidfile)
            return  # not an error in a restart

        # Try killing the daemon process
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError as err:
            err = str(err)
            if err.find("No such process") > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print(str(err))
                sys.exit(1)

    def restart(self):
        """
        Restart the daemon
        """
        self.stop()
        self.start()

    def run(self):
        """
        You should override this method when you subclass Daemon. It will be called after the process has been
        daemonized by start() or restart().
        """

    def quit(self):
        """
        You should override this method when you subclass Daemon. It will be called before the process is stopped.
        """


class testdaemon(Daemon):
    def run(self, path):
        sys.stderr.write(path)
        logging.debuf(path)
        
        with open(path, mode='w', newline='') as file_out:
            try:
                while True:


                    scanned_code = barcode_reader()
                    if scanned_code:
                        file_out.write(scanned_code + "\n")
                        file_out.flush()
                    #     print(f"Сохранено: {scanned_code}")
                    sys.stderr.write(f"Сохранено: {scanned_code}")
                    # time.sleep(10)
                        
            except KeyboardInterrupt:
                logging.debug('Keyboard interrupt')
            except Exception as err:
                logging.error(err)

daemon = testdaemon()

if 'start' == sys.argv[1] and sys.argv[2]:
    daemon.start(path = sys.argv[2])
elif 'start' == sys.argv[1] :
    daemon.start()
elif 'stop' == sys.argv[1]:
    daemon.stop()
elif 'restart' == sys.argv[1]:
    daemon.restart()
    
    # def quit(self):
    #    ...