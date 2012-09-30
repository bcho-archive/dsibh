#coding: utf-8

from os import path

from processing import read, process


s = process(read(path.join('testcase', '5.example')))
