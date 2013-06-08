#!/usr/bin/env python2
#-*- coding: utf-8 -*-

import random

import dfs.client

if __name__ == '__main__':
    fp = '/wtf/test'
    f = dfs.client.open(fp, 'w')
    f.write('tro lol\n')
    f.close()
