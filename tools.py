#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 23:12:30 2018

@author: childrenbody
"""
import pandas as pd
import gc
import numpy as np

class train_info():
    '''
    展示一些train样本的信息。
    '''
    def __init__(self):
        self.train = pd.read_csv('input/[new] yancheng_train_20171226.csv')

    def date_class(self) -> 'dict type':
        '''
        每个月份参与销售的车型数量。
        '''
        date = self.train.sale_date.unique()
        date_class = {d: self.train[self.train.sale_date == d].class_id.nunique() for d in date}
        return date_class

    def class_sale_date(self, class_id, plot=False) -> 'array type':
        '''
        车型ID为class_id的销售月份。
        '''
        temp = self.train[self.train.class_id == class_id][['sale_date', 'class_id', 'sale_quantity']]
        result = temp['sale_date'].unique()
        if plot:
            temp['sale_date'] = pd.to_datetime(temp['sale_date'], format='%Y%m')
            temp.plot(x='sale_date', y='sale_quantity')
        return result
    
    def uninterrupted(self, class_id, show_interrupted_month=False):
        '''
        查询该车型历史销售月份有没有中断，返回缺失的月份。
        '''
        sale_date = sorted(self.train.sale_date.unique(), reverse=True)
        class_date = set(self.train[self.train.class_id == class_id].sale_date.unique())
        earliest = min(class_date)
        sale_date = set(sale_date[:sale_date.index(earliest) + 1])
        return len(sale_date) == len(class_date), list(sale_date.difference(class_date))
        
    def interrupted_month(date: 'str by "," split') -> 'uninterrupted months, str':
        '''
        从201710开始，返回连续的月份。
        '''
        date = map(int, date.split(','))
        date = sorted(date, reverse=True)
        for i in range(len(date) - 1):
            if date[i] - date[i + 1] not in [1, 89]:
                return date[:i+1]
        else:
            return date

def expend(data, feature, label, multiple, noise) -> 'dataframe':
    '''
    
    '''
    label = data[label]
    data = data[feature]
    gc.collect()
    temp_data = pd.DataFrame()
    temp_label = pd.DataFrame()
    for i in range(multiple - 1):
        temp = data.as_matrix() + (np.random.random(data.shape) - 0.5)*2*noise
        temp = pd.DataFrame(temp)
        temp.columns = data.columns
        temp_data = pd.concat([temp_data, temp], axis=0)
        temp_label = pd.concat([temp_label, label], axis=0)
    data = pd.concat([data, temp_data], axis=0)
    label = pd.concat([label, temp_label], axis=0)
    return pd.concat([data, label], axis=1)
