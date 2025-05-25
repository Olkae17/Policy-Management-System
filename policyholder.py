# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 05:04:54 2025

@author: Olkae
"""

class Policyholder:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.active = True
        self.products = []
        self.payments = []

    def suspend(self):
        self.active = False

    def reactivate(self):
        self.active = True

    def add_product(self, product):
        self.products.append(product)

    def add_payment(self, payment):
        self.payments.append(payment)

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Active: {self.active}")
        print("Products:")
        for p in self.products:
            print(f" - {p.name}")
        print("Payments:")
        for p in self.payments:
            print(f" - ${p.amount} on {p.date}")
