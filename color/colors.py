import sys
import ctypes

STD_OUTPUT_HANDLE = -11

def get_csbi_attributes(handle):
    import struct
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr,
    left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhhhhhhhh", csbi.raw)
    return wattr

def color(text, color, nl = True):
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    sys.stdout.write(text)
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)
    if nl: print("")
    sys.stdout.flush()

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)


# more functions here

def pc(t, c = 0xf, nl = True):
    t = str(t)
    color(t,c, nl)

def debug():
    pass # Figure out how to get stupid LMS vars

def info(i):
    print(str(i))