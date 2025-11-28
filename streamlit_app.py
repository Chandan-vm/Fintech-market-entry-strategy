import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="FinTech Market Entry Strategy Dashboard", layout="wide")

st.title("📊 FinTech Market Entry Strategy & Competitor Benchmarking Dashboard")
st.write("A Deloitte-style consulting analysis project.")

# Load competitor data
df = pd.read_csv("competitor_data.csv")

tab1, tab2, tab3, tab4 = st.tabs(["Market Share", "Pricing Models", "Turnaround Time", "Insights & Recommendations"])

with tab1:
    st.subheader("📌 Market Share by Competitor")
    fig = px.bar(df, x="Company", y="Market_Share", color="Company", title="Market Share (%)")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("💰 Pricing Models Overview")
    st.dataframe(df[["Company", "Pricing_Model"]])

with tab3:
    st.subheader("⏱ Turnaround Time Comparison")
    fig2 = px.bar(df, x="Company", y="Turnaround_Time", color="Turnaround_Time", title="Faster Approval Times Are More Competitive")
    st.plotly_chart(fig2, use_container_width=True)

with tab4:
    st.subheader("📌 SWOT Insights")
    st.write("""
    **Strengths:**  
    • Strong demand for instant digital credit  
    • High smartphone & UPI penetration  
    • Low customer acquisition cost in digital channels  

    **Weaknesses:**  
    • High NPA risk  
    • Regulatory uncertainty  
    • Dependence on risk algorithms  

    **Opportunities:**  
    • Credit inclusion for thin-file customers  
    • BNPL expansion  
    • AI-driven underwriting  

    **Threats:**  
    • Heavy competition  
    • Interest rate hikes  
    • Data privacy rules  
    """)

    st.subheader("📌 Recommendations")
    st.write("""
    ✔ Enter with a low-cost, fast-approval model  
    ✔ Target young professionals & Gen-Z  
    ✔ Build partnerships with e-commerce & wallet apps  
    ✔ Use AI-based dynamic risk scoring  
    ✔ Offer subscription-based loyalty plans  
    """)
