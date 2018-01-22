#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:56:59 2018

@author: childrenbody
"""
import pandas as pd

# result/1.2.1.csv
# 取九月份和十月份的零售量。九月份权重为0.4，十月份为0.6。
October = pd.read_csv('result/1.0.csv')
September = pd.read_csv('result/1.1.csv')
o = October.predict_quantity.as_matrix()
s = September.predict_quantity.as_matrix()
result = October[['predict_date', 'class_id']]
result['predict_quantity'] = o*0.6 + s*0.4
result.to_csv('result/1.2.1.csv', index=False)


# =============================================================================
# # result/1.2.csv
# # 取九月份和十月份零售量的均值。
# October = pd.read_csv('result/1.0.csv')
# September = pd.read_csv('result/1.1.csv')
# o = October.predict_quantity.as_matrix()
# s = September.predict_quantity.as_matrix()
# result = October[['predict_date', 'class_id']]
# result['predict_quantity'] = (o + s)/2
# result.to_csv('result/1.2.csv', index=False)
# =============================================================================

# =============================================================================
# # result/1.0.csv
# # 把2017年11月的数据作为结果提交，相同型号车的销量相加。 
# train = pd.read_csv('input/[new] yancheng_train_20171226.csv')
# test = pd.read_csv('input/yancheng_testA_20171225.csv')
# temp = train[train.sale_date == 201710][['class_id', 'sale_quantity']]
# result = temp.groupby(['class_id']).agg(sum).reset_index()
# for i, row in test.iterrows():
#     test.at[i, 'predict_quantity'] = result[result.class_id == row.class_id].sale_quantity
# test.to_csv('result/1.0.csv', index=False)
# =============================================================================

