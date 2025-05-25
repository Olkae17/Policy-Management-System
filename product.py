# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 05:04:55 2025

@author: Olkae
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.active = True

    def update_price(self, new_price):
        self.price = new_price

    def suspend(self):
        self.active = False
