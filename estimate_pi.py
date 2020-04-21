#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:29:40 2020

@author: tonyguang
"""


def estimate_pi(n):
    num_point_circle = 0
    num_point_total = 0
    for n in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1 :
            num_point_circle += 1
        num_point_total += 1

    return 4 * num_point_circle/num_point_total

estimate_pi(10)

estimate_pi(1000)

estimate_pi(10000)

estimate_pi(100000)

estimate_pi(1000000)

estimate_pi(10000000)