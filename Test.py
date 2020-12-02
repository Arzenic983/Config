import sys
from SQLreq import *

from PartTypes import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


def part_setup(part_name):  # part_name берётся из комбобокса
    global obj
    typo, ID = get_type(part_name), get_id(part_name)
    info = get_info(part_name, typo.lower(), ID)
    info.remove(info[2])
    try:
        if typo == 'CPU':
            cpu = CPU(info[0], info[1], info[2], info[3], info[4], info[5])
            obj = cpu
        if typo == 'MTRBRD':
            motherboard = MTRBRD(info[0], info[1], info[2], info[3], info[4],
                                info[5], info[6], info[7], info[8], info[9], info[10])
            obj = motherboard
        if typo == 'GPU':
            gpu = GPU(info[0], info[1], info[2], info[3], info[4],
                            info[5], info[6], info[7], info[8])
            obj = gpu
        if typo == 'RAM':
            ram = RAM(info[0], info[1], info[2], info[3], info[4], info[5], info[6])
            obj = ram
        if typo == 'COOLER':
            cooler = COOLER(info[0], info[1], info[2], info[3], info[4], info[5])
            obj = cooler
        if typo == 'CORPUS':
            corpus = CORPUS(info[0], info[1], info[2], info[3], info[4])
            obj = corpus
        if typo == 'STRG':
            storage = STRG(info[0], info[1], info[2], info[3])
            obj = storage
        if typo == 'PWRSPL':
            power_supply = PWRSPL(info[0], info[1], info[2], info[3], info[4], info[5])
            obj = power_supply
    except:
        obj = ''
        return obj

b = 'Proton 600w'

part_setup(b)
try:
    a = obj.da_print(b)
except:
    a = 'Process finished with exit code 0xc000007b'
print(a)