# -*- coding: utf-8 -*
import pandas as pd
#倒入路径
catering_sale = '../data/catering_sale.xls'
#倒入Excel
data = pd.read_excel(catering_sale, index_col = u'日期')
#描述基本资料
data.describe()
