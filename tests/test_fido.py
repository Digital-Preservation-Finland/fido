#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fido.fido import PerfTimer


def test_perf_timer():
    timer = PerfTimer()
    x = 1000000
    while x:
        x -= 1
    duration = timer.duration()
    assert duration > 0
