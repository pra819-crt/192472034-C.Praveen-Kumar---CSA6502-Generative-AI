import pandas as pd

data = {
    "Name": ["Ram", "Sam", "Tom", "Ravi"],
    "Marks": [85, 90, None, 75]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

df = df.dropna()

print("\nCleaned Data")
print(df)

print("\nAverage Marks =", df["Marks"].mean())

print("Highest Marks =", df["Marks"].max())
