# Q14. In a study of the effects of caffeine on reaction time, a sample of 30 participants had an average
# reaction time of 0.25 seconds with a standard deviation of 0.05 seconds. Conduct a hypothesis test to
# determine if the caffeine has a significant effect on reaction time at a 90% confidence level using a t-test.

# Answer - 
import scipy.stats as stat
sample_size = 30 
sample_mean = 0.25
std = 0.05
confidence_value = 90
critical_value = 1.645

# Null hyposthesis = population mean = 0 (there is no significance chaange)
# alternate hyposthesis = population mean >0 

t_stats = (sample_mean-0)/(std/(sample_size**0.5))
print(t_stats)

if t_stats > critical_value:
    print("Reject the Null hypothesis")
else:
    print("Accept the Null Hypothesis")