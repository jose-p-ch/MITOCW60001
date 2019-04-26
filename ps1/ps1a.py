# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
current_savings = 0.0
month_count = 0
r = 0.04
while current_savings < portion_down_payment * total_cost:
    current_savings += current_savings * r / 12 + annual_salary / 12 * portion_saved
    month_count += 1
print(month_count)