import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

rainfall = []

for month in months:
    value = input(f"Enter rainfall for {month} (mm): ")
    rainfall.append(float(value))

with open("rainfall.txt", "w") as file:
    for value in rainfall:
        file.write(f"{value}\n")

rainfall = []
with open("rainfall.txt", "r") as file:
    for line in file:
        rainfall.append(float(line.strip()))

color = ['#FF6B9D', '#FFB36B', '#9C6BFF', '#6BFFC6', '#115365',
         '#10C50A', '#833EA5', '#B80541', '#F4F14F', '#84B1F6',
         '#F808AC', '#40296C']

wettest_month = months[rainfall.index(max(rainfall))]
dryest_month = months[rainfall.index(min(rainfall))]

plt.figure(figsize=(12, 6), facecolor="white")
bars = plt.bar(months, rainfall, color=color, edgecolor="black", width=0.85, linewidth=2)
plt.title("Monthly Rainfall Distribution", fontsize=16, fontweight='bold')
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.axhline(y=sum(rainfall) / len(rainfall), color='green', linestyle='--',
            label=f'Average: {sum(rainfall) / len(rainfall):.1f}')
plt.ylim(0, max(rainfall) + 20)
plt.legend()
plt.grid(True, alpha=0.3)

ax = plt.gca()
ax.set_facecolor("#ffbebe")
ax.bar_label(bars, padding=3, fontsize=11, fontweight="bold", color="black")

print(f"wettest month: {wettest_month} ({max(rainfall)}/mm)")
print(f"dryest month: {dryest_month} ({min(rainfall)}/mm)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("rainfall_chart.png")
print("finish project")