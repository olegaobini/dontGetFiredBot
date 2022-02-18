
import colorama
from random import seed
from colorama import Fore, Style

seed()
colorama.init(wrap=False)
COLOR_HEADER = Fore.MAGENTA
COLOR_OKBLUE = Fore.BLUE
COLOR_OKGREEN = Fore.GREEN
COLOR_REPORT = Fore.YELLOW
COLOR_FAIL = Fore.RED
COLOR_ENDC = Style.RESET_ALL
COLOR_BOLD = Style.BRIGHT