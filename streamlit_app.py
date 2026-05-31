import streamlit as st
import pandas as pd

# 1. Create a web title
st.title("My First Web Analytics Dashboard")

# 2. Simulate data (like an inline Qlik load script)
data = {
    'Year': [2023, 2024, 2025, 2026],
    'Sales': [100, 150, 220, 310]
}
df = pd.DataFrame(data)

# 3. Create a web sidebar dropdown filter
selected_year = st.sidebar.selectbox("Select Year Filter", df['Year'])

# 4. Display a dynamic data table and a line chart
st.write(f"Showing data. Selected filter: {selected_year}")
st.line_chart(df.set_index('Year'))
