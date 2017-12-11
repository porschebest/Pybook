# -*- coding: utf-8 -*
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import GSD

#初始化模型
model = Sequential()
#添加输入层(20个节点)、第一隐藏层(64个节点)的连接

model.add(Dense(20, 64))
#第一隐藏层使用tanh作为激活函数
model.add(Activation('tanh'))
#使用dropout防止過拟合
model.add(dropout(0.5))

#添加第一隱藏層(64节点)、第二隐藏层(64个节点)的连接
model.add(Dense(64,64))
#第二隐藏层使用tanh作为激活函数
model.add(Activation('tanh'))
#使用dropout防止過拟合
model.add(dropout(0.5))

#添加第二隱藏層(64節點)、輸出層(1節點)的連接
model.add(Dense(64,1))
#输出层使用sigmoid作为激活函数
model.add(Activation('sigmoid'))

#定义求解演算法
sgd = SGD(1r=0.1, decay=1e-6, momentum=0.9, nesterov=True)
#编译生成模型，损失函数为平均误差平方和
model.compile(loss='mean_squared_error', optimizer=sgd)
#训练模型
model.fit(X_train, y_train, nb_epoch=20, batch_size=16)
#测试模型
score = model.evaluate(X_test, y_test, batch_size=16)

"""
model.pridict() 训练模型
model.predict_classes() 分类跌果
"""
