import streamlit as st
import pandas as pd

# Title of the app
st.title("Simple Streamlit and Pandas App")

# Create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "San Francisco", "Chicago"]
}
df = pd.DataFrame(data)

# Display the DataFrame
st.write("Here's a sample DataFrame:")
st.dataframe(df)

# Add a filter option
age_filter = st.slider("Filter by Age", 20, 40, 30)
filtered_df = df[df["Age"] <= age_filter]

st.write(f"Filtered Data (Age <= {age_filter}):")
st.dataframe(filtered_df)
