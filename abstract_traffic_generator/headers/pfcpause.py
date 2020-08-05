from typing import *


class PfcPause(object):
    """PFC pause traffic header

    Args
    ----
    dst (str): Destination mac address  
    src (str): Source mac address  
    eth_type (str): Ethernet type  
    ctl_op_code (str): Control operation code  
    pri_en_vec (str): Priority enable vector  
    queue0 (str): Pause quanta queue 0  
    queue1 (str): Pause quanta queue 1  
    queue2 (str): Pause quanta queue 2  
    queue3 (str): Pause quanta queue 3  
    queue4 (str): Pause quanta queue 4  
    queue5 (str): Pause quanta queue 5  
    queue6 (str): Pause quanta queue 6  
    queue7 (str): Pause quanta queue 7  
    """

    def __init__(self, 
        dst: str = '0180c2000001', 
        src: str = '0000aa000001', 
        eth_type: str = '8808', 
        ctl_op_code: str = '0101',
        pri_en_vec: str = '01', 
        queue0: str = 'ffff', 
        queue1: str = '00', 
        queue2: str = '00',
        queue3: str = '00', 
        queue4: str = '00', 
        queue5: str = '00', 
        queue6: str = '00', 
        queue7: str = '00'):
        self.type = 'PFCPAUSE'
        self.dst = dst
        self.src = src
        self.eth_type = eth_type
        self.ctl_op_code = ctl_op_code
        self.pri_en_vec = pri_en_vec
        self.queue0 = queue0
        self.queue1 = queue1
        self.queue2 = queue2
        self.queue3 = queue3
        self.queue4 = queue4
        self.queue5 = queue5
        self.queue6 = queue6
        self.queue7 = queue7
        
