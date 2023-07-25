student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas as pd


studednt_data_frame = pd.DataFrame(student_dict)
print(studednt_data_frame)


# # Loop through a data frmae

# for (key, value) in studednt_data_frame.items():
#     print(value)


# Loop through rows of a data frame

for (index, row) in studednt_data_frame.iterrows():
    print(row.student)
