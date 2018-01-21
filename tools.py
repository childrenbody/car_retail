#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 23:12:30 2018

@author: childrenbody
"""
import pandas as pd

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

    def class_sale_date(self, class_id) -> 'array type':
        '''
        车型ID为class_id的销售月份。
        '''
        return self.train[self.train.class_id == class_id]['sale_date'].unique()
        
        
