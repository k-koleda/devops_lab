import time
import datetime
import psutil
import ConfigParser
import threading


def cur_time():
    """get current time"""
    c_time = time.time()
    return datetime.datetime.fromtimestamp(c_time).strftime('%Y-%m-%d %H:%M:%S')


def cpu():
    """get usage cpu per core"""
    return psutil.cpu_percent(interval=1, percpu=True)


def mem_v():
    """get usage virt memory in MB"""
    return psutil.virtual_memory().used / (1024.0 ** 3)


def mem_p():
    """get usage phy memory in MB"""
    return psutil.swap_memory().used / (1024.0 ** 3)


def io():
    """get info about io disk"""
    return psutil.disk_io_counters()


def net():
    """get info about network"""
    return psutil.net_io_counters(pernic=True)


def output():
    """write result in file"""
    result = "SNAPSHOT: {0}: CPU per core {1}: Virtual memory used: {2} Physical memory used:' \
          ' {3} IO info: (Read bytes: {4}, Write bytes: {5})' \
          ' Network info: (Bytes Sent: {6} Bytes Resv: {7}) " \
        .format(cur_time(), cpu(), mem_p(), mem_p(), io()[3], io()[4], net()['lo'][0], net()['lo'][1])
    file = open("testfile.txt", "a")
    file.write(result + "\n")
    file.close()


def read_param():
    """read param from file"""
    config = ConfigParser.ConfigParser()
    config.read("param.txt")
    config.sections()
    dict1 = {}
    options = config.options("common")
    for option in options:
        dict1[option] = config.get("common", option)
    return dict1


interval = int(read_param()['interval'])
output_f = read_param()['output']


def main_fun():
    """run timer and main tasks"""
    threading.Timer(interval, main_fun).start()
    read_param()
    output()


main_fun()





