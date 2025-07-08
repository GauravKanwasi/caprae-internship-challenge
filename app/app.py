import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import io

# Set page config
st.set_page_config(page_title="Caprae Lead Generator", layout="wide")

# Load data
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(project_root, "data", "enriched_leads.csv")
df = pd.read_csv(data_path)

# Header with logo
st.image("https://via.placeholder.com/150x50?text=Caprae+AI", width=150)
st.title("Caprae Lead Generator 🚀")
st.markdown("Filter high-quality leads for SaaS & M&A outreach")

# Filters
col1, col2 = st.columns(2)
with col1:
    industry_filter = st.selectbox("🔍 Filter by Industry", ["All"] + list(df["Industry"].unique()))
with col2:
    job_title_filter = st.selectbox("🔍 Filter by Job Title", ["All"] + list(df["Job Title"].unique()))

# Apply filters
if industry_filter != "All":
    df = df[df["Industry"] == industry_filter]
if job_title_filter != "All":
    df = df[df["Job Title"] == job_title_filter]

# Display filtered data
st.markdown("### 📋 Filtered Leads")
st.dataframe(df, use_container_width=True)

# Visualizations
st.markdown("### 📊 Data Insights")
col3, col4 = st.columns(2)

with col3:
    st.markdown("#### Industry Distribution")
    fig, ax = plt.subplots()
    sns.countplot(data=df, y="Industry", ax=ax, hue="Industry", palette="viridis", legend=False)
    st.pyplot(fig)

with col4:
    st.markdown("#### Age Distribution")
    if "Age" in df.columns:
        fig, ax = plt.subplots()
        sns.histplot(df["Age"], bins=20, ax=ax, kde=True, color="teal")
        st.pyplot(fig)
    else:
        st.warning("Age data not found. Ensure `data_enrichment.py` was run successfully.")

# Export options
st.markdown("### 📤 Export Options")
col5, col6 = st.columns(2)

with col5:
    st.download_button(
        label="Export to CSV",
        data=df.to_csv(index=False),
        file_name=f"{industry_filter}_{job_title_filter}_leads.csv",
        mime="text/csv"
    )

with col6:
    excel_buffer = io.BytesIO()
    df.to_excel(excel_buffer, index=False, engine='xlsxwriter')
    st.download_button(
        label="Export to Excel",
        data=excel_buffer.getvalue(),
        file_name=f"{industry_filter}_{job_title_filter}_leads.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# Footer
st.markdown("---")
st.markdown("Developed for Caprae Capital Intern Challenge | Built with 🚀 [Streamlit]( https://streamlit.io/ )")
