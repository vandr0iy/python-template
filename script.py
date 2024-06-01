#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is a template for python scripts"""
import itertools
import os
import random
import sys
import time

spinner = itertools.cycle(["-", "/", "|", "\\"])

env_FOO = os.environ.get("FOO", None)
print(f"the value of FOO is {env_FOO}")
print("---")

def long_running_method(size=100):
    """All this method does is returning an arbitrarily-sized list of prandom integers"""
    result = [None for y in range(size)]
    try:
        for i in range(0, size):
            time.sleep(0.05)
            result[i] = random.randint(1, size - 1)
            if i % 10 == 0:
                print(f"\t{i}%…", end="\r", flush=True)
            print(next(spinner), end="\r", flush=True)
        print("\tDONE!")
    except Exception as e: # pylint: disable=broad-exception-caught
        print(f"cant complete: {e}")
        sys.exit(1)
    return result


def main():
    """This invokes the long_running_method, and then prints out the result"""
    print("Starting the function run!")
    print("long_running_method is running…")
    prandom_ints = long_running_method()
    print("the result is:")
    for idx, val in enumerate(prandom_ints):
        print(f"{val: 3}", end=",")
        if (idx + 1) % 10 == 0:
            print()
    print()
    print("result printed out successfully!\n")

if __name__ == "__main__":
    main()
