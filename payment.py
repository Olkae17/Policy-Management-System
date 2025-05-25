# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 05:04:56 2025

@author: Olkae
"""

from datetime import date

class Payment:
    def __init__(self, amount):
        self.amount = amount
        self.date = date.today()

    def send_reminder(self):
        print("Reminder: Your payment is due.")

    def apply_penalty(self, penalty):
        self.amount += penalty
        print(f"A penalty of ${penalty} has been added.")
