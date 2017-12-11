# -*- coding: utf-8 -*

#导入ADF检验
from statsmodels.tsa.stattools import adfuller as ADF
from pandas.core import datetools
import numpy as np
ADF(np.random.rand(100))
