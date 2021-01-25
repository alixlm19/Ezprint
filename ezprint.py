from sys import stdout 

def set_decoration(bold:bool=False, underline:bool=False, inverted:bool=False):
    decoration=""
    if bold:
        decoration += "\033[1m"
    if underline:
        decoration += "\033[4m"
    if inverted:
        decoration += "\033[7m"
    stdout.write(decoration)
    
def cprint(msg:any, *args,
fcolor:int=255,
bcolor:int=0,
bold:bool=False,
underline:bool=False,
inverted:bool=False,
reset:bool=True):

    if any((bold, underline, inverted)):
        set_decoration(bold, underline, inverted)
    
    formated_msg = f"\033[38;5;{fcolor}m"
    if bcolor:
        formated_msg += f"\033[48;5;{bcolor}m"

    formated_msg += msg
    if reset:
        formated_msg += "\033[0m"
    for arg in args:
        formated_msg += str(arg)
    stdout.write(formated_msg + "\n")
