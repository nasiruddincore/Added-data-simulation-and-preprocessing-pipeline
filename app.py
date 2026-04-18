import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Retail & Sales Dashboard", layout="wide")


# ==============================
# Safe Load Function
# ==============================
def load_dataset(file_path):
    if not os.path.exists(file_path):
        return None

    if os.stat(file_path).st_size == 0:
        return None

    try:
        df = pd.read_csv(file_path)

        if df.empty:
            return None

        df.columns = df.columns.str.lower()
        return df

    except Exception:
        return None


# ==============================
# Detect Columns
# ==============================
def detect_columns(df):
    date_col = 'date' if 'date' in df.columns else None

    value_col = None
    for col in ['sales', 'qty_sold', 'revenue', 'amount']:
        if col in df.columns:
            value_col = col
            break

    return date_col, value_col


# ==============================
# Clean Data
# ==============================
def clean_data(df, date_col, value_col):
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df[value_col] = pd.to_numeric(df[value_col], errors='coerce')
    df = df.dropna(subset=[date_col, value_col])
    df = df.sort_values(by=date_col)
    return df


# ==============================
# Plot Functions
# ==============================
def plot_trend(df, x, y):
    fig, ax = plt.subplots()
    ax.plot(df[x], df[y])
    ax.set_title("Trend")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)


def plot_distribution(df, col):
    fig, ax = plt.subplots()
    ax.hist(df[col], bins=20)
    ax.set_title("Distribution")
    st.pyplot(fig)


def plot_boxplot(df, col):
    fig, ax = plt.subplots()
    ax.boxplot(df[col])
    ax.set_title("Boxplot")
    st.pyplot(fig)


def plot_scatter(df, x, y):
    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y])
    ax.set_title("Scatter")
    st.pyplot(fig)


# ==============================
# Dashboard Section
# ==============================
def show_dashboard(df, name):
    if df is None:
        st.warning(f"{name} dataset not found or empty")
        return

    date_col, value_col = detect_columns(df)

    if date_col is None or value_col is None:
        st.error(f"{name}: Required columns not found")
        st.write(df.columns)
        return

    df = clean_data(df, date_col, value_col)

    st.subheader(name)

    st.dataframe(df.head(), width='stretch')

    col1, col2, col3 = st.columns(3)
    col1.metric("Records", len(df))
    col2.metric("Average", round(df[value_col].mean(), 2))
    col3.metric("Max", df[value_col].max())

    colA, colB = st.columns(2)

    with colA:
        plot_trend(df, date_col, value_col)
        plot_boxplot(df, value_col)

    with colB:
        plot_distribution(df, value_col)
        plot_scatter(df, date_col, value_col)


# ==============================
# MAIN APP
# ==============================
def main():
    st.title("Retail & Sales Analytics Dashboard")

    retail_df = load_dataset("data/retail_data.csv")
    sales_df = load_dataset("data/sales_data.csv")

    tab1, tab2 = st.tabs(["Retail Data", "Sales Data"])

    with tab1:
        show_dashboard(retail_df, "Retail Data")

    with tab2:
        show_dashboard(sales_df, "Sales Data")


if __name__ == "__main__":
    main()