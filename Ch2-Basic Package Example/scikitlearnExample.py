# -*- coding: utf-8 -*
# 导入线性回归模型
from sklearn.linear_model import LinearRegression
#导入数据集
from sklearn import datasets
#导入svm 模型
from sklearn import svm

#---------Example1-----------
#建立线性回归模型
model = LinearRegression()
print(model)
"""
其他函数
训练模型-
model.fit()

监督式学习：fit(X,y)
model.predict(X_new) 预测新样本
model.predict_proba(X_new) 预测概率
model.score() 得分越高，fit越好

非监督式学习：fit(X)
model.transform() 学到新的基空间
model.fit_transform()
从数据中学到的新的基，并将这个数据
按照这组「基」进行转换
"""
#---------Example2-----------
#加载数据集
iris = datasets.load_iris()
#查看数据集大小
print(iris.data.shape)

#---------Example3-----------
#建立线性SVM分类气
clf = svm.LearnSVC()
#用数据训练模型
clf.fit(iris.data, iris.target)
#输入数据进行预测
clf.predict([5.0, 3.6, 1.3, 0.25])
#查看训练好的模型的参数
clf.coef_
