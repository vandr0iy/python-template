#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools
import json
import math
import os
import random
import requests
import sys
import time

spinner = itertools.cycle(['-', '/', '|', '\\'])

env_FOO = os.environ.get('FOO', None)
print(f'the value of FOO is {env_FOO}')
print('---')

def long_running_method(size=100):
    result = [None for y in range(size)]
    try:
        for i in range(0,size):
            time.sleep(0.05)
            result[i] = random.randint(1,size-1)
            if i % 10 == 0:
                print(f'\t{i}%…', end='\r', flush=True)
            print(next(spinner), end='\r', flush=True)
        print(f'\tDONE!')
    except Exception as e:
        print(f'cant complete: {e}')
        sys.exit(1)
    return result

def start():
    print('Starting the function run!')
    print('long_running_method is running…')
    foo=long_running_method()
    print('the result is:')
    for idx,val in enumerate(foo):
        print(f'{val: 3}', end=',')
        if (idx + 1) % 10 == 0:
            print()
    print()
    print(f'result printed out successfully!\n')
            
start()
