#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""

"""

from bank_class import *

file='bankStatement.txt'


def main():


    myBankAccount = BankAccount('Cesar','Sinchiguano',300.0)
    print(myBankAccount.name.firstname+' '+myBankAccount.name.lastname)
    myBankAccount.deposit(20.0)
    print'Deposit:',myBankAccount.money
    print'Balance:'+str(myBankAccount.get_Balance())

    print(myBankAccount.name.firstname+' '+myBankAccount.name.lastname)
    myBankAccount.withdraw(10.0)
    print'Withdraw:',myBankAccount.money
    print'Balance:'+str(myBankAccount.get_Balance())

    print('======Bank Statement======')
    with open(file, 'r') as f:
        for line in f:
            print line+'\n',

if __name__=='__main__':
    main()
