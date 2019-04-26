# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:46:30 2019

@author: josep
"""
def partB(annual_salary, portion_search):
    #annual_salary = float(input("Enter your annual salary: "))
    portion_saved = portion_search / 10000.0
    total_cost = 1000000.0
    semi_annual_raise = 0.07
    portion_down_payment = 0.25
    current_savings = 0.0
    month_count = 0
    r = 0.04
    while current_savings < portion_down_payment * total_cost:
        current_savings += current_savings * r / 12 + annual_salary / 12 * portion_saved
        month_count += 1
        if month_count % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
    return month_count

annual_salary = float(input("Enter the starting salary: "))
steps = 1
guess = 10000
guess_portion = guess
months = partB(annual_salary, guess)
if months > 36:
    print("It is not possible to pay the down payment in three years.")
else:
    while months != 36:
        guess_portion /= 2
        steps += 1
        #print(guess)
        if months < 36:
            guess -= guess_portion
            months = partB(annual_salary, guess)
        else:
            guess += guess_portion
            months = partB(annual_salary, guess)
final_guess = int(guess)
print("Best savings rate: ", final_guess/10000)
print("Steps in bisection search: ", steps)