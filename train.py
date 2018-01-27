#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 13:42:15 2018

@author: childrenbody
"""
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
import gc
from tools import expend

# =============================================================================
# # result/2.1.csv
# # 用三个月的销量作为特征，后一个月的销量作为目标。这里只用2017年7月以后的样本。
# train = pd.read_csv('data/month_sale.csv')
# train = train[train.sale_date >= 201707]
# less_car = [194201, 359378, 376193, 653436, 725137]
# train['less'] = train.class_id.apply(lambda x: x in less_car)
# less = train[train['less']]
# more = train[train.less == False]
# result = less[less.sale_date == 201710]
# result.drop(['sale_date', 'less'], axis=1, inplace=True)
# result.columns = ['class_id', 'predict_quantity']
# data = pd.DataFrame({'class_id': more.class_id.unique(),
#                     '201707': more[more.sale_date == 201707].sale_quantity.tolist(),
#                     '201708': more[more.sale_date == 201708].sale_quantity.tolist(),
#                     '201709': more[more.sale_date == 201709].sale_quantity.tolist(),
#                     '201710': more[more.sale_date == 201710].sale_quantity.tolist()})
# del train, less, more
# gc.collect()
# test = data[['201708', '201709', '201710', 'class_id']]
# data = expend(data, ['201707', '201708', '201709'], ['class_id', '201710'], 100, 0.1)
# x_train, x_test, y_train, y_test = train_test_split(data[['201707', '201708', '201709']].as_matrix(), data['201710'].tolist(), test_size=0.3)
# watch_train = xgb.DMatrix(x_train, y_train)
# watch_test = xgb.DMatrix(x_test, y_test)
# watchlist = [(watch_train, 'train'), (watch_test, 'test')]
# xgbtrain = xgb.DMatrix(data[['201707', '201708', '201709']].as_matrix(), data['201710'].tolist())
# xgbtest = xgb.DMatrix(test[['201708', '201709', '201710']].as_matrix())
# res = test[['class_id']]
# del data, x_train, x_test, y_train, y_test, test
# gc.collect()
# param = {'objective': 'reg:linear',
#          'eval_metric': 'rmse'
#         }
# model = xgb.train(param, xgbtrain, 10, watchlist)
# res['predict_quantity'] = model.predict(xgbtest)
# result = pd.concat([result, res], axis=0)
# test = pd.read_csv('input/yancheng_testA_20171225.csv')
# test.drop(['predict_quantity'], axis=1, inplace=True)
# test = pd.merge(test, result, on=['class_id'])
# test.to_csv('result/2.1.csv', index=False)
# =============================================================================

# =============================================================================
# # result/2.0.csv
# # 用前一个月和该车型的销售的月份数作为特征，后一个月作为目标。
# train = pd.read_csv('input/[new] yancheng_train_20171226.csv')
# test = pd.read_csv('input/yancheng_testA_20171225.csv')
# test.drop(['predict_quantity'], axis=1, inplace=True)
# 
# september = train[train.sale_date == 201709][['class_id', 'sale_quantity']].groupby('class_id').agg(sum).reset_index()
# october = train[train.sale_date == 201710][['class_id', 'sale_quantity']].groupby('class_id').agg(sum).reset_index()
# september['months'] = september.class_id.apply(lambda x: train[train.class_id == x].sale_date.nunique() - 2)
# october['months'] = october.class_id.apply(lambda x: train[train.class_id == x].sale_date.nunique() - 1)
# 
# x_train, x_test, y_train, y_test = train_test_split(september[['sale_quantity', 'months']], october['sale_quantity'], test_size=0.3)
# 
# watch_train = xgb.DMatrix(x_train, y_train)
# watch_test = xgb.DMatrix(x_test, y_test)
# watch_list = [(watch_train, 'train'), (watch_test, 'test')]
# xgbtrain = xgb.DMatrix(september[['sale_quantity', 'months']], october['sale_quantity'])
# xgbtest = xgb.DMatrix(october[['sale_quantity', 'months']])
# param = {
#         'objective': 'reg:linear',
#         'eval_metric': 'rmse'
#         }
# model = xgb.train(param, xgbtrain, 10, watch_list)
# october['predict_quantity'] = model.predict(xgbtest)
# result = pd.merge(test, october[['class_id', 'predict_quantity']], on=['class_id'])
# result.to_csv('result/2.0.csv', index=False)
# =============================================================================
