import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('C:/projects/ML-AI/Project/Fitness Tracker Data Analysis/data.csv')
df['Date'] = pd.to_datetime(df['Date']) # Convert 'Date' column to datetime format

# Print basic info
print("Dataset Head:")
print(df.head())  # Display first few rows of the dataset

# # Add a NumPy column: Calories per minute
df['CaloriesPerMin'] = df['Calories'] / df['Duration'] 

# # Filter: High calorie burn
high_cal_burn = df[df['Calories'] > 400] 

# # Summary statistics
print("\n Summary Statistics:")
print(df.describe()) #df.describe() provides a summary of the dataset like count, mean, std, min, max, etc.

# Plot 1: Calories burned over time
plt.figure(figsize=(10, 5)) 
plt.plot(df['Date'], df['Calories'], marker='o', color='green') 
plt.title('Calories Burned Over Time')
plt.xlabel('Date')
plt.ylabel('Calories')
plt.grid(True)
plt.tight_layout()
plt.savefig("calories_over_time.png")
plt.show()

# Plot 2: Pulse vs. Calories
plt.figure(figsize=(6, 4)) 
plt.scatter(df['Pulse'], df['Calories'], c='red')
plt.title('Pulse vs Calories Burned')
plt.xlabel('Pulse')
plt.ylabel('Calories')
plt.grid(True)
plt.tight_layout()
plt.savefig("pulse_vs_calories.png")
plt.show()
