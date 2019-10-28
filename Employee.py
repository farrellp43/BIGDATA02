# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 08:53:28 2019

@author: Asus
"""

class Employee:
    
    def __init__(self, first, last):
        if self.__class__ == Employee:
            raise NotImplementedError
            
        self.firstname = first
        self.lastname = last
        
    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)
    
    def _checkPositive(self, value):
        if value < 0:
            raise ValueError
            
        else:
            return value
        
    def earnings(self):
        raise NotImplementedError
        
class Boss(Employee):
    
    def __init__(self, first, last, salary):
        Employee.__init__(self, first, last)
        self.weeklySalary = self._checkPositive(float(salary))
        
    def earnings(self):
        return self.weeklySalary
    
    def __str__(self):
        return "%17s: %s" % ("Boss", Employee.__str__(self))
    
class CommissionWorker(Employee):
    
    def __init__(self, first, last, salary, commission, quantity):
        Employee.__init__(self, first, last)
        self.salary = self._checkPositive(float(salary))
        self.commission = self._checkPositive(float(commission))
        self.quantity = self._checkPositive(quantity)
        
    def earnings(self):
        return self.salary + self.commission + self.quantity
    
    def __str__(self):
        return "%17s: %s" % ("Commission Worker", Employee.__str__(self))
    
class PieceWorker(Employee):
    
    def __init__(self, first, last, wage, quantity):
        Employee.__init__(self, first, last)
        self.wagePerPiece = self._checkPositive(float(wage))
        self.quantity = self._checkPositive(quantity)
        
    def earnings(self):
        return self.quantity * self.wagePerPiece
    
    def __str__(self):
        return "%17s: %s" % ("Piece Worker", Employee.__str__(self))
    
class HourlyWorker(Employee):
    
    def __init__(self, first, last, wage, hours):
        Employee.__init__(self, first, last)
        self.wage = self._checkPositive(float(wage))
        self.hours = self._checkPositive(float(hours))
        
    def earnings(self):
        if self.hours <= 40:
            return self.wage * self.hours
        else:
            return 40 * self.wage + (self.hours - 40) * self.wage * 1.5
        
    def __str__(self):
        return "%17s: %s" % ("Hourly Worker", Employee.__str__(self))
    
employees = [ Boss("John", "Smith", 800.00),
              CommissionWorker("Sue", "Jones", 200.0, 3.0, 150),
              PieceWorker("Bob", "Lewis", 2.5, 200),
              HourlyWorker("Karen", "Price", 13.75, 40)]

for anjing in employees:
    print ("%s earned $%.2f" % (anjing, anjing.earnings()))
            
        
        
        
        
        