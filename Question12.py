# Q12. A researcher is testing the effectiveness of two different teaching methods on student performance.
# Sampel A has a mean score of 85 with a standard deviation of 6, while sample B has a mean score of 82
# with a standard deviation of 5. Conduct a hypothesis test to determine if the two teaching methods have a
# significant difference in student performance using a t-test with a significance level of 0.01.

import scipy.stats as stat

sample_mean1 = 85
std1 = 6
sample_mean2 = 82
std2 = 5

t_stats,p_value=stat.ttest_ind_from_stats(mean1=sample_mean1,std1=std1,mean2=sample_mean2,std2=std2,nobs1=10,nobs2=10)
print(t_stats)
print(p_value)

if t_stats>p_value:
    print("Reject the NUll hypothesis")
else:
    print("accept the null hypothesis")