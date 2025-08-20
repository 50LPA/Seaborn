# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# 1. Generate synthetic seasonal revenue data
# -----------------------------
np.random.seed(42)

months = pd.date_range("2024-01-01", periods=24, freq="ME")
revenue = 100 + 10*np.sin(np.linspace(0, 4*np.pi, 24)) + np.random.normal(0, 3, 24)

df = pd.DataFrame({
    "Month": months,
    "Revenue": revenue
})

# -----------------------------
# 2. Set Seaborn styling
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")
palette = sns.color_palette("crest")

# -----------------------------
# 3. Create professional lineplot
# -----------------------------
plt.figure(figsize=(8, 8))  # ensures 512x512 with dpi=64
sns.lineplot(data=df, x="Month", y="Revenue", marker="o")

plt.title("Seasonal Revenue Trends", fontsize=18, weight="bold")
plt.xlabel("Month")
plt.ylabel("Revenue (in $K)")
plt.xticks(rotation=45)

# -----------------------------
# 4. Save chart
# -----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
