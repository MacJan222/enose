import pandas as pd


original_df = pd.read_excel("./dataverse_files/dataset_12.xlsx")


list1 = original_df[original_df.Label == 1]
list2 = original_df[original_df.Label == 2]
list3 = original_df[original_df.Label == 3]
list4 = original_df[original_df.Label == 4]

print(list4)