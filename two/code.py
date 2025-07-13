import pandas as pd
from scipy import stats

df = pd.read_csv("data.csv")
conf_level = 0.95
a, b = (df["group_a"], df["group_b"])

t_stat, p_val = stats.ttest_ind(a,b)

print("T-statistic >>", t_stat)
print("P-value >>", p_val)

def result_interpret(p_val, conf_level):
    if p_val < 1 - conf_level:
        return "There is a significant difference between the 2 groups."
    else:
        return "There is no significant difference between the 2 groups."

print(result_interpret(p_val, conf_level))

