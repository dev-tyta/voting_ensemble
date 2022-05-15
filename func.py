from sklearn.preprocessing import OrdinalEncoder


def sort_missing(data):
    col_null = []
    column = list(data.columns)
    for col in column:
        if data[col].isna().sum() > 0:
            col_null.append(col)
    mode = []
    for miss in col_null:
        mode.append(data[miss].mode())
    real_mode = []
    for modes in mode:
        real_mode.append(modes[0])
    val = {}
    for miss in col_null:
        for m in real_mode:
            val[miss] = m
            real_mode.remove(m)
            break
    for i, k in val.items():
        data[i].fillna(k, inplace=True)
    return data.isnull().sum()


def categ_data(data):
    s = (data.dtypes == 'object')
    obj_col = list(s[s].index)
    ordinal = OrdinalEncoder()
    data[obj_col] = ordinal.fit_transform(data[obj_col])
    return data.head()
