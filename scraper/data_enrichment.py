import pandas as pd
import os
from datetime import datetime

def validate_data(df):
    # Deduplicate and validate
    df = df.drop_duplicates()
    df["valid_email"] = df["Email"].str.contains("@")
    df["phone_clean"] = df["Phone"].str.replace(r"[^\d+]", "", regex=True)
    return df

def map_job_titles(df):
    # Map job titles to industries (Caprae’s focus areas)
    industry_mapping = {
        "Data scientist": "SaaS",
        "Software engineer": "SaaS",
        "Machine learning engineer": "AI/ML",
        "Biomedical engineer": "HealthTech",
        "Corporate investment banker": "M&A",
        "IT technical support officer": "SaaS",
        "Database administrator": "SaaS"
    }
    df["Industry"] = df["Job Title"].map(industry_mapping).fillna("Other")
    return df

def calculate_age(df):
    # Convert "Date of birth" to datetime and calculate age
    df["Date of birth"] = pd.to_datetime(df["Date of birth"], errors="coerce")
    current_year = datetime.now().year
    df["Age"] = current_year - df["Date of birth"].dt.year
    return df

if __name__ == "__main__":
    # Use absolute paths to avoid FileNotFound errors
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_path = os.path.join(project_root, "data", "people-1000.csv")
    output_path = os.path.join(project_root, "data", "enriched_leads.csv")
    
    df = pd.read_csv(input_path)
    df = validate_data(df)
    df = map_job_titles(df)
    df = calculate_age(df)  # Adds Age column
    df.to_csv(output_path, index=False)
