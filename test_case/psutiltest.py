import psutil

print("cpu_count:",psutil.cpu_count())
print("cpu_percent",psutil.cpu_percent())

print("cpu信息",psutil.cpu_times())

print("内存",psutil.virtual_memory())
print("进程",psutil.pids())


