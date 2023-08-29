# Q11. In a survey of 500 people, 65% reported being satisfied with their current job. Calculate the 95%
# confidence interval for the true proportion of people who are satisfied with their job.

sample_size = 500
sample_proportion = 0.65

# confidence_interval = sample proportion +- (z*standard error ) 

z = 1.96

lower_confidence_interval = 0.65 - (1.96 * 0.0276)
upper_confidence_interval = 0.65 + (1.96 * 0.0276)
print(lower_confidence_interval, upper_confidence_interval)

