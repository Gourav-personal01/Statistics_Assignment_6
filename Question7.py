# Q7. Calculate the 95% confidence interval for a sample of data with a mean of 50 and a standard deviation
# of 5. Interpret the results.

# Answer - we will calculate the confidence interval in which the unkknown confidence interval lie.

mean = 50 
standard_deviation = 5 
sample_size = 30 # assume

#confidence_interval = mean +- margin of error 

critial_value = 1.96

lower_confidence_interval = mean - critial_value * (5/(30**0.5))
print(lower_confidence_interval)

higher_confidence_interval = mean + critial_value * (5/(30**0.5))
print(higher_confidence_interval)

# the unknown population mean is lies between in the confidence interval (48.2 and 51.7)