# -*- coding: utf-8

from os import times, sysconf_names, sysconf

print "Hello World!"

f = open('/proc/uptime')
for line in f:
    s = line.split(' ')
    uptime = float(s[0])
f.close()

f = open('/proc/self/stat')
for line in f:
    s = line.split(' ')
    starttime = float(s[21])
f.close()

freq = sysconf(sysconf_names['SC_CLK_TCK'])

print(times(), 'Total elapsed time[s]:', format(float(uptime - (starttime / freq)), '.3g'))

f = open('/proc/self/io')
for line in f:
    s = line.split(':')
    if s[0] in ['rchar', 'wchar', 'read_bytes', 'write_bytes']:
        # print(line, format(float(s[1]), '.2g'), end='')
        print(s[0], "{:,}".format(int(s[1])), format(float(s[1]), '.2g'))
f.close()

f = open('/proc/self/status')
for line in f:
    s = line.split(':')
    if s[0] in ['VmPeak', 'VmSize', 'VmHWM', 'VmRSS', 'VmSwap']:
        t = str.split(s[1], ' ')
        print(s[0], "{:,}".format(int(t[-2])), str(t[-1])[:-1])
        # HWM High Water Mark
        # TODO: use locale for 1000 separator
f.close()

# $ nuitka --recurse-all --recurse-stdlib --exe Hello_world.py
# $ rm -r Hello_world.build/
