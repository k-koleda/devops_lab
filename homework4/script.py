import time
import datetime
import psutil
import ConfigParser
import threading


class Snapshot:
    def __init__(self):
        self.interval = int(self.read_param()['interval'])
        self.output_f = self.read_param()['output']


    def cur_time(self):
        """get current time"""
        c_time = time.time()
        return datetime.datetime.fromtimestamp(c_time).strftime('%Y-%m-%d %H:%M:%S')


    def cpu(self):
        """get usage cpu per core"""
        return psutil.cpu_percent(interval=1, percpu=True)


    def mem_v(self):
        """get usage virt memory in MB"""
        return psutil.virtual_memory().used / (1024.0 ** 3)


    def mem_p(self):
        """get usage phy memory in MB"""
        return psutil.swap_memory().used

    def io(self):
        """get info about io disk"""
        return psutil.disk_io_counters()


    def net(self):
        """get info about network"""
        return psutil.net_io_counters(pernic=True)


    def output(self):
        """write result in file"""
        result = "SNAPSHOT: {0}: CPU per core {1}: Virtual memory used: {2} Physical memory used: {3}" \
                 " IO info: (Read bytes: {4}, Write bytes: {5}) Network info: (Bytes Sent: {6} Bytes Resv: {7}) " \
        .format(self.cur_time(), self.cpu(), self.mem_v(), self.mem_p(), self.io()[3], self.io()[4], self.net()['lo'][0], self.net()['lo'][1])
        file = open("testfile.txt", "a")
        file.write(result + "\n")
        file.close()


    def read_param(self):
        """read param from file"""
        config = ConfigParser.ConfigParser()
        config.read("param.txt")
        config.sections()
        dict1 = {}
        options = config.options("common")
        for option in options:
            dict1[option] = config.get("common", option)
        return dict1


    def main_fun(self):
        """run timer and main tasks"""
        threading.Timer(self.interval, self.main_fun).start()
        self.read_param()
        self.output()



Snapshot().main_fun()
print("Script running")
