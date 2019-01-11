import frida
rdev = frida.get_remote_device()
processes = rdev.enumerate_processes()
for process in processes:
    print process