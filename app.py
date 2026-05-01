import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_cleaning import clean_data
from utils.kpi_calculator import calculate_kpis
from utils.insight_generator import generate_insights

st.set_page_config(page_title="AI Executive Dashboard Generator", layout="wide")

st.title("AI Executive Dashboard Generator")
st.write("Upload a messy CRM or sales CSV and generate executive-level insights.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Data Preview")
    st.dataframe(df.head())

    cleaned_df = clean_data(df)

    st.subheader("Cleaned Data Preview")
    st.dataframe(cleaned_df.head())

    kpis = calculate_kpis(cleaned_df)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${kpis['total_revenue']:,.0f}")
    col2.metric("Average Deal Size", f"${kpis['avg_deal_size']:,.0f}")
    col3.metric("Win Rate", f"{kpis['win_rate']:.1f}%")
    col4.metric("Pipeline Value", f"${kpis['pipeline_value']:,.0f}")

    st.subheader("Revenue by Month")
    revenue_month = cleaned_df.groupby("month")["deal_value"].sum().reset_index()
    fig1 = px.line(revenue_month, x="month", y="deal_value", markers=True)
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Deals by Stage")
    fig2 = px.bar(cleaned_df, x="stage", y="deal_value", color="stage")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Revenue by Customer Segment")
    segment_revenue = cleaned_df.groupby("customer_segment")["deal_value"].sum().reset_index()
    fig3 = px.pie(segment_revenue, names="customer_segment", values="deal_value")
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("AI-Generated Executive Insights")
    insights = generate_insights(cleaned_df, kpis)

    for insight in insights:
        st.write(f"- {insight}")
else:
    st.info("Upload a CSV file to begin.")
