# Q13. A population has a mean of 60 and a standard deviation of 8. A sample of 50 observations has a mean
# of 65. Calculate the 90% confidence interval for the true population mean.

# Answer - 

population_mean = 60
std = 8 
sample_size = 50 
sample_mean = 65
z_value = 1.645

higher_confidence_level = sample_mean + (z_value * std/(sample_mean**0.5))
print(higher_confidence_level)

lower_confidence_level = sample_mean - (z_value * std/(sample_mean**0.5))
print(lower_confidence_level)
