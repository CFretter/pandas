"""
Tests that NA values are properly handled during
parsing for all of the parsers defined in parsers.py
"""
from io import StringIO

import numpy as np
import pytest

from pandas._libs.parsers import STR_NA_VALUES

from pandas import DataFrame, Index, MultiIndex
import pandas._testing as tm

### https://github.com/pandas-dev/pandas/issues/32134
def test_na_affects_precision(all_parsers):
    parser = all_parsers
    TESTDATA1 = StringIO("""col1;col2
     1;123
     2;456
     3;1582218195625938945
     """)
    TESTDATA2 = StringIO("""col1;col2
     1;123
     2;
     3;1582218195625938945
     """)
    result1 = parser.read_csv(TESTDATA1, sep=";", dtype={'col2':'Int64'})
    result2 = parser.read_csv(TESTDATA2, sep=";", dtype={'col2':'Int64'})

    n1 = result1.loc[2,'col2'] 
    n2 = result2.loc[2,'col2']
    assert(n1==n2)
