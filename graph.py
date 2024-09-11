import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, spearmanr

mean_time_spent = [444, 2216, 2361, 2018, 2487, 805, 1437, 1803, 2146]
llm_carbon_footprint = [2.387, 15.325, 19.773, 16.151, 19.810, 4.774, 14.456, 19.291, 19.349]
manual_carbon_footprint = [0.1203, 0.6003, 0.6401, 0.5472, 0.6756, 0.2181, 0.3894, 0.4888, 0.5820]

ratio_carbon_footprint = [m / l for m, l in zip(llm_carbon_footprint, manual_carbon_footprint)]

plt.figure(figsize=(10, 6))
plt.scatter(mean_time_spent, ratio_carbon_footprint, color='purple')
# plt.plot(mean_time_spent, ratio_carbon_footprint, color='purple', linestyle='--')

plt.title('Task Complexity vs. Ratio of LLM to Manual Carbon Footprint')
plt.xlabel('Task Complexity (Mean Time Spent)')
plt.ylabel('Ratio of Manual to LLM Carbon Footprint')

pearson_corr, pearson_p_value = pearsonr(mean_time_spent, ratio_carbon_footprint)

# Spearman correlation
spearman_corr, spearman_p_value = spearmanr(mean_time_spent, ratio_carbon_footprint)

# Print results
slope, intercept = np.polyfit(mean_time_spent, ratio_carbon_footprint, 1)
line_of_best_fit = np.array(mean_time_spent) * slope + intercept

# Plot the line of best fit
plt.plot(mean_time_spent, line_of_best_fit, color='orange', label=f'Best fit line (r={pearson_corr:.2f})')
plt.grid(True)

plt.show()
print(f"Pearson Correlation Coefficient: {pearson_corr}, p-value: {pearson_p_value}")
print(f"Spearman Correlation Coefficient: {spearman_corr}, p-value: {spearman_p_value}")
