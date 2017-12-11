# -*- coding: utf-8 -*
import pandas as pd

#创建一个序列s
s = pd.Series([1, 2, 3], index=['a','b','c'])

#创建一个表格 d
d = pd.DataFrame([[1 ,2 ,3],[4, 5 ,6]], columns = ['a','b','c'])

#用已有的序列来创建表格
d2 = pd.DataFrame(s)

#预览前五行数据
d.head()
#数据机本统计量
d.describe()

#读取文件，注意问见的储存路径不能带有中文，否则读取可能出错
pd.read_excel('data.xls')
pd.read_csv('data.csv', encoding='utf-8')
