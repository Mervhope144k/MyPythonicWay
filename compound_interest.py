#!/usr/bin/python3

# Calculate the compound interest after t years

original_principal_sum = 10000
compound_frequency = 12
annual_interest_rate = 0.08
time = int(input("Enter the length of time the interest is applied is: "))
new_principal_sum = original_principal_sum * ((1 + (annual_interest_rate / compound_frequency)) ** (compound_frequency * time))
print("The new principal sum is ", new_principal_sum, "$") 
