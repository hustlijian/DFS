#!/usr/bin/env python2
#-*- coding: utf-8 -*-
import logging

import dfs.client

if __name__ == '__main__':
    with dfs.client.open('/wtf/test') as f:
        logging.info(f.read())
