import pandas as pd

def validate_emails(df):
    df["valid_email"] = df["email"].str.contains("@")
    return df

def filter_high_quality_leads(df, target_industry="SaaS"):
    return df[df["industry"] == target_industry]

if __name__ == "__main__":
    df = pd.read_csv("data/leads.csv")
    df = validate_emails(df)
    df = filter_high_quality_leads(df, target_industry="SaaS")
    df.to_csv("data/filtered_leads.csv", index=False)