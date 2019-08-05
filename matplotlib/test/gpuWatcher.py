import matplotlib.pyplot as plt
import numpy as np
import re
import collections

#import matplotlib.animation

g_watchWin = 60

DEBUG_DRI_PATH='/sys/kernel/debug/dri/'
nodeIndex='0'
powerNode = 'amdgpu_pm_info'


class PowerEntry:
    def __init__(self):
        self.value = 0
        self.queue = collections.deque([0 for i in range(g_watchWin)])

class PowerInfo:
    def __init__(self):
        #self.fileName = DEBUG_DRI_PATH + nodeIndex + '/' + powerNode
        self.fileName = powerNode
        self.powerNode = ''

        self.mclk = PowerEntry()
        self.sclk = PowerEntry()
        self.vddgfx = PowerEntry()
        self.temp = PowerEntry()
        self.list = [self.mclk,
                     self.sclk,
                     self.vddgfx,
                     self.temp]

    def update_power_info(self):
        fileName = powerNode
        with open(fileName, 'r') as f:
            for line in f.readlines():
                print(line)
                if line.find("(MCLK)") != -1:
                    self.mclk.value = re.findall('\d+', line)[0]
                    self.update_power_entry(self.mclk)
                elif line.find("(SCLK)") != -1:
                    self.sclk.value = re.findall('\d+', line)[0]
                    self.update_power_entry(self.sclk)
                elif line.find("(VDDGFX)") != -1:
                    self.vddgfx.value = re.findall('\d+', line)[0]
                    self.update_power_entry(self.vddgfx)
                elif line.find("GPU Temperature:") != -1:
                    self.temp.value = re.findall('\d+', line)[0]
                    self.update_power_entry(self.temp)

    def update_power_entry(self, entry):
        entry.queue.rotate(-1)
        entry.queue.pop()
        entry.queue.append(entry.value)

    def find_power_node(self):
        # TODO: find power node in debugfs
        self.powerNode = ''

t = range(g_watchWin)
#queue = collections.deque([0 for i in range(60)])

N_ROW, N_COL = 2, 2
fig, axes = plt.subplots(N_ROW, N_COL, figsize=(9, 6))
#fig, axes = plt.subplots()


pi = PowerInfo()

for i in range(100):
    index = 0
    pi.update_power_info()

    fig.clear()

    for i in range(N_ROW * N_COL):
        index += 1
        plt.subplot(N_ROW, N_COL, index)
        plt.plot(t, list(pi.list[i].queue))

    plt.pause(1)

plt.close()


## working !!!
#def update(i):
#    with open(fileName, 'r') as f:
#        for line in f.readlines():
#            if line.find("(MCLK)") != -1:
#                mclk = re.findall('\d+', line)[0]
#
#    queue.rotate(-1)
#    queue.pop()
#    queue.append(mclk)
#    fig.clear()
#    plt.plot(t, list(queue))
#
#ani = matplotlib.animation.FuncAnimation(fig, update, interval=1000, repeat=True)
#plt.show()

