from random import seed
import colorama
from colorama import Fore, Style
from PIL import Image, ImageDraw
import numpy as np
from subprocess import check_output
import sys

seed()
colorama.init(wrap=False)
COLOR_HEADER = Fore.MAGENTA
COLOR_OKBLUE = Fore.BLUE
COLOR_OKGREEN = Fore.GREEN
COLOR_REPORT = Fore.YELLOW
COLOR_FAIL = Fore.RED
COLOR_ENDC = Style.RESET_ALL
COLOR_BOLD = Style.BRIGHT

def screenshot(device, path):
    device.screenshot(path)

def similar_arr_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if elem.size == myarr.size and np.allclose(elem, myarr)), False)

def checkImage(path, width, height):
    image = Image.open(path)
    if width == None and height == None:
        return np.array(image, dtype=np.uint8)
    else:
        return np.array(image, dtype=np.uint8)[width][height]


#TODO FIX THIS
def getDimensions(device):
    return device.window_size()


def colorCheck(width, height, *args):
    pass