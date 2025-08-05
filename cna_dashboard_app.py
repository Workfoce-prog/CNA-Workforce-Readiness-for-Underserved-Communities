
import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("CNA_Curriculum_Dashboard_Data.csv")

st.set_page_config(page_title="CNA Student Progress Dashboard", layout="wide")

st.title("📘 CNA Student Progress Dashboard")

# Sidebar filters
st.sidebar.header("🔍 Filter Options")
selected_section = st.sidebar.selectbox("Select Curriculum Section", options=["All"] + sorted(df["Section"].unique()))
selected_rag = st.sidebar.multiselect("Filter by RAG Progress", options=df["RAG_Progress"].unique(), default=df["RAG_Progress"].unique())

# Filter data
filtered_df = df.copy()
if selected_section != "All":
    filtered_df = filtered_df[filtered_df["Section"] == selected_section]
if selected_rag:
    filtered_df = filtered_df[filtered_df["RAG_Progress"].isin(selected_rag)]

# Display filtered table
st.dataframe(filtered_df, use_container_width=True)

# RAG Level Chart
st.subheader("📊 RAG Progress Summary")
rag_summary = filtered_df["RAG_Progress"].value_counts().reset_index()
rag_summary.columns = ["RAG Level", "Count"]
st.bar_chart(rag_summary.set_index("RAG Level"))

# Quiz score distribution
st.subheader("📝 Quiz Score Distribution")
st.line_chart(filtered_df.groupby("Section")["Student_Score"].mean())
