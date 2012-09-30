#coding: utf-8

from frac import frac_factory
from elimination import Equation, Equations


def read(fn):
    f = file(fn, 'r')
    ret = f.readlines()
    f.close()
    return ret


def write(content, dest):
    f = file(dest, 'w')
    f.write(content)
    f.close()
    return


def process(lines):
    '''Read the linear equations system from input and return a Equations system'''
    system = Equations()
    for line in lines:
        equation = Equation([frac_factory(i) for i in line.split()])
        system.append(equation)
    return system
