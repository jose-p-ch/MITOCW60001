# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:46:30 2019

@author: josep
"""
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))
portion_down_payment = 0.25
current_savings = 0.0
month_count = 0
r = 0.04
while current_savings < portion_down_payment * total_cost:
    current_savings += current_savings * r / 12 + annual_salary / 12 * portion_saved
    month_count += 1
    if month_count % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
print(month_count)