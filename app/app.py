import streamlit as st
import pandas as pd

st.title("Caprae Lead Generator")
st.markdown("Filter high-quality leads for SaaS & M&A outreach")

df = pd.read_csv("../data/filtered_leads.csv")
industry = st.selectbox("Select Industry", df["industry"].unique())
filtered_df = df[df["industry"] == industry]

st.dataframe(filtered_df)
st.download_button(
    label="Export Filtered Leads",
    data=filtered_df.to_csv(index=False),
    file_name=f"{industry}_leads.csv",
    mime="text/csv"
)