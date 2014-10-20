#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Wei Wang"
__email__ = "tskatom@vt.edu"

import sys
import os
import pandas as pd

def dict2series(data_obj, resample='D'):
    series = pd.Series(data_obj)
    series.index = pd.DatetimeIndex(series.index)
    series = series.resample(resample, how='sum').fillna(0)
    return series

if __name__ == "__main__":
    pass

