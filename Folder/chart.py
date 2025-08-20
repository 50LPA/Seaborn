# chart.py
# Author email: 24f1002855@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set Seaborn style and context for professional look
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic business data: Seasonal revenue pattern
np.random.seed(42)
months = pd.date_range(start="2023-01-01", periods=12, freq="ME")
revenue = (
    20000 + 5000 * np.sin(np.linspace(0, 2 * np.pi, 12))  # seasonal trend
    + np.linspace(0, 4000, 12)  # growth trend
    + np.random.normal(0, 1500, 12)  # noise
)

df = pd.DataFrame({
    "Month": months.strftime("%b"),
    "Revenue": revenue
})

# Create the lineplot
plt.figure(figsize=(8, 8))  # 8x8 inches @ dpi=64 => 512x512 pixels
sns.lineplot(
    data=df,
    x="Month",
    y="Revenue",
    marker="o",
    linewidth=2.5,
    color="royalblue"
)

# Customize chart
plt.title("Monthly Revenue Trend (Synthetic Data)", fontsize=16, weight="bold")
plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue (USD)", fontsize=12)
plt.xticks(rotation=45)

# Save chart
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
