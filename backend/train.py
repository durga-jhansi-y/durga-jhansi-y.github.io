# here we r going to tarin the ML models 
import pandas as pd
import os

# Path to the data folder
data_path = "data"

# Example: Load the main training and test files
train_file = os.path.join(data_path, "KDDTrain+.txt")
test_file = os.path.join(data_path, "KDDTest+.txt")

# Load datasets (no headers in these files)
train_df = pd.read_csv(train_file, header=None)
test_df = pd.read_csv(test_file, header=None)

# Quick look at the data
print("Training data shape:", train_df.shape)
print("Test data shape:", test_df.shape)
print(train_df.head())
