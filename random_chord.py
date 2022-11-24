#!/usr/bin/python3
"""
Created on Tue Aug 28 22:00:19 2018

@author: Eve
"""
import random
import time


def do_loop(tones, types, wait=5):
    loop = 100
    for i in range(loop):
        rtone = random.choice(tones)
        rtype = random.choice(types)
        chord = "{}{}".format(rtone, rtype)
        print(chord)
        time.sleep(wait)

def ex1():
    wait = 5
    tones = ["G", "C"]
    types = ["7", "M7", "m7", "m7b5", "dim7", "6", "m6"]
    do_loop(tones, types, wait)

def ex2():
    wait = 5
    tones = ["G", "C", "D", "A"]
    types = ["7", "M7", "m7", "m7b5", "dim7", "6", "m6"]
    do_loop(tones, types, wait)

def ex3():
    # D strings chords
    wait = 5
    tones = ["F"]
    types = ["7", "M7", "m7", "m7b5", "dim7", "6", "m6"]
    do_loop(tones, types, wait)

def ex4():
    # 3 strings variants, with 9 chords
    wait = 5
    tones = ["G", "C", "F"]
    types = ["7", "M7", "m7", "m7b5", "dim7", "6", "m6", "9", "m9", "9", "m9"]
    do_loop(tones, types, wait)

def ex5():
    # 3 strings, 2 positions (3 and 5)
    wait = 5
    tones = ["G", "A", "C", "D", "F", "E"]
    types = ["7", "M7", "m7", "m7b5", "dim7", "6", "m6", "9", "m9"]
    do_loop(tones, types, wait)

def ex6():
    # Other positions (2 and 5)
    wait = 5
    tones = ["F#", "A", "B", "D", "E"]
    types = ["7", "M7", "m7", "m7b5", "dim7", "6", "m6", "9", "m9"]
    do_loop(tones, types, wait)

def ex7():
    # New chord types
    wait = 10
    tones = ["G", "C", "F"]
    types = ["7sus4", "6/9", "7b9", "7#9"]
    do_loop(tones, types, wait)

if __name__ == '__main__':
    ex7()
