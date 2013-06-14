#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os, sys
from pkg1.mu1 import mod_one

def test_m():
    print('this is module demo start...')
    m_1 = mod_one()
    m_1.f1()


if __name__ == '__main__':
    test_m()

