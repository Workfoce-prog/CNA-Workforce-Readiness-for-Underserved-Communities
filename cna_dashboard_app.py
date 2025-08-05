import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("CNA_Curriculum_Dashboard_Data.csv")

# RAG thresholds
def get_rag_status(score):
    if score >= 85:
        return "🟢 Excellent"
    elif score >= 70:
        return "🟡 Good"
    elif score >= 50:
        return "🟠 Needs Improvement"
    else:
        return "🔴 High Risk"

# App title
st.title("📘 CNA Student Dashboard")
st.markdown("Track your progress, test yourself, and get recommendations.")

# Student ID selection
student_id = st.selectbox("Select Your Student ID", df["Student_ID"].unique())
student_data = df[df["Student_ID"] == student_id].iloc[0]

# Display performance
st.subheader("📊 Your Progress")
st.write(f"**Module 1 Score:** {student_data['Module_1_Score']}% — {get_rag_status(student_data['Module_1_Score'])}")
st.write(f"**Module 2 Score:** {student_data['Module_2_Score']}% — {get_rag_status(student_data['Module_2_Score'])}")
st.write(f"**Module 3 Score:** {student_data['Module_3_Score']}% — {get_rag_status(student_data['Module_3_Score'])}")
st.write(f"**Module 4 Score:** {student_data['Module_4_Score']}% — {get_rag_status(student_data['Module_4_Score'])}")

# Overall performance
average_score = student_data[["Module_1_Score", "Module_2_Score", "Module_3_Score", "Module_4_Score"]].mean()
rag = get_rag_status(average_score)

st.subheader("⭐ Overall Performance")
st.metric(label="Average Score", value=f"{average_score:.1f}%", delta=None)
st.write(f"**RAG Status:** {rag}")

# Recommendation
st.subheader("✅ Recommended Actions")
st.write(student_data["Recommendation_Action"])

# Visualization
import matplotlib.pyplot as plt

# Pie chart for score distribution
labels = ["Module 1", "Module 2", "Module 3", "Module 4"]
scores = [student_data["Module_1_Score"], student_data["Module_2_Score"],
          student_data["Module_3_Score"], student_data["Module_4_Score"]]

fig1, ax1 = plt.subplots()
ax1.pie(scores, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

# Line chart to simulate trend (static for demo)
trend_data = pd.DataFrame({
    "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
    "Score": [60, 70, 75, average_score]
})
st.line_chart(trend_data.set_index("Week"))