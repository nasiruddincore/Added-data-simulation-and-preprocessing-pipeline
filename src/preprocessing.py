def clean_data(df):
    df = df.drop_duplicates()
    df = df[df["qty_sold"] >= 0]
    df = df.fillna(0)
    return df