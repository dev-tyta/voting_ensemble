def miss_values(data)
col_null = []
column = list(loan_df.columns)
print(column)
for col in column:
    if loan_df[col].isna().sum() > 0:
        col_null.append(col)
print(col_null)
mode = []
for miss in col_null:
    mode.append(loan_df[miss].mode())
print(mode)
real_mode = []
for modes in mode:
    real_mode.append(modes[0])
print(real_mode)