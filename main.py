import pandas as pd
import matplotlib.pyplot as plt
import os


def load_dataset(path):
    if not os.path.exists(path):
        return None

    if os.stat(path).st_size == 0:
        return None

    try:
        df = pd.read_csv(path)

        if df.empty:
            return None

        df.columns = df.columns.str.lower()
        return df

    except Exception:
        return None


def detect_columns(df):
    date_col = 'date' if 'date' in df.columns else None

    value_col = None
    for col in ['sales', 'qty_sold', 'revenue', 'amount']:
        if col in df.columns:
            value_col = col
            break

    return date_col, value_col


def clean_data(df, date_col, value_col):
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df[value_col] = pd.to_numeric(df[value_col], errors='coerce')
    df = df.dropna(subset=[date_col, value_col])
    df = df.sort_values(by=date_col)
    return df


def visualize(df, name):
    if df is None:
        print(f"{name} dataset not found or empty")
        return

    date_col, value_col = detect_columns(df)

    if date_col is None or value_col is None:
        print(f"{name}: Required columns missing")
        print(df.columns)
        return

    df = clean_data(df, date_col, value_col)

    print(f"\n{name} Visualization")

    # Trend
    plt.figure()
    plt.plot(df[date_col], df[value_col])
    plt.title(f"{name} Trend")
    plt.xticks(rotation=45)
    plt.show()

    # Distribution
    plt.figure()
    plt.hist(df[value_col], bins=20)
    plt.title(f"{name} Distribution")
    plt.show()

    # Boxplot
    plt.figure()
    plt.boxplot(df[value_col])
    plt.title(f"{name} Boxplot")
    plt.show()

    # Scatter
    plt.figure()
    plt.scatter(df[date_col], df[value_col])
    plt.title(f"{name} Scatter")
    plt.xticks(rotation=45)
    plt.show()


def main():
    retail_df = load_dataset("data/retail_data.csv")
    sales_df = load_dataset("data/sales_data.csv")

    visualize(retail_df, "Retail Data")
    visualize(sales_df, "Sales Data")


if __name__ == "__main__":
    main()