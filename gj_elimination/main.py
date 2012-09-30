#coding: utf-8

# TODO FEATURES
# Yeah, needs some cool cli options, such as:
# 
#   - read from file
#   - write to file
#   - display format
#   - ...
#

from processing import process


def _read():
    lines = []
    while 1:
        try:
            lines.append(raw_input())
        except EOFError:
            break
    return lines


def _main():
    #print process(_read()).solve
    ret = process(_read())
    print ret.solve


if __name__ == '__main__':
    _main()
