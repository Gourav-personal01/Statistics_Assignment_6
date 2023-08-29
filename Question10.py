# Q10. In a study of the effectiveness of a new weight loss drug, a sample of 50 participants lost an average
# of 6 pounds with a standard deviation of 2.5 pounds. Conduct a hypothesis test to determine if the drug is
# significantly effective at a 95% confidence level using a t-test.

import scipy.stats as stat

sample_size = 50
sample_mean = 6
population_mean = 0
std = 2.5
confidence_interval = 0.95

# Null Hypothesis = mean = 6
# alternate hypotheis = mean =! 6 

dof = sample_size -1

critical_value = 2.021

t_value = (sample_mean - population_mean)/(std/(sample_size**0.5))
print(t_value)

if t_value > critical_value:
    print("Reject the Null hypothesis")
else:
    print("Accept the Null hypothesis")