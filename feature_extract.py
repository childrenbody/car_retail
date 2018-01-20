#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:56:59 2018

@author: childrenbody
"""
import pandas as pd
from collections import Counter



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

