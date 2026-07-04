import pickle

with open("feature_columns (1).pkl", "rb") as f:
    feature_columns = pickle.load(f)

print(len(feature_columns))
print(feature_columns)