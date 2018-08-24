#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""
class Name():
    def __init__(self,name=None,lastname=None):
        self.firstname=name
        self.lastname=lastname

class BankAccount:
    def __init__(self, name=None,lastname=None, balance = 0.0):
        self.log("Bank account has been created!")
        self.name = Name(name,lastname)
        self.balance = balance
        self.money=0.0

    def get_Balance(self):
        self.log("Balance checked at " + str(self.balance))
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.money=amount
        self.log("+" + str(amount) + ": " + str(self.balance))

    def withdraw(self, amount):
        self.balance -= amount
        self.money=amount
        self.log("-" + str(amount) + ": " + str(self.balance))

    def log(self, data):
        file=open('bankStatement.txt','a')
        file.write(data+'\n')
        file.close()
