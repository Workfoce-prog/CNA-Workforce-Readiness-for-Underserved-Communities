
import streamlit as st
import pandas as pd
import random

# Load data
df = pd.read_csv("CNA_Curriculum_Dashboard_Data.csv")

st.set_page_config(page_title="CNA Student Learning Hub", layout="wide")
st.title("🎓 CNA Student Learning & Progress Hub")

# Section selector
section = st.selectbox("📘 Choose a CNA Section to Learn", sorted(df["Section"].unique()))
section_df = df[df["Section"] == section].reset_index(drop=True)

# Topic navigator
topic = st.selectbox("🧠 Select a Topic", section_df["Topic"])
topic_data = section_df[section_df["Topic"] == topic].iloc[0]

st.markdown(f"### 📝 Topic: {topic}")
st.markdown(f"**What You'll Learn:** {topic_data['Details & Examples']}")

# Quiz time
st.markdown("---")
st.subheader("🧪 Quick Knowledge Check")

user_answer = st.text_input(f"**Quiz:** {topic_data['Quick Quiz Question']}")
if user_answer:
    if user_answer.strip().lower() in topic_data["Answer"].lower():
        st.success("✅ Correct! Great job! 🎉")
    else:
        st.error(f"❌ Not quite. The correct answer is: **{topic_data['Answer']}**")

# Show student score, RAG, and recommendation
st.markdown("---")
st.subheader("📊 Your Progress & Support")

st.metric(label="Your Score (Mock)", value=topic_data["Student_Score"])
st.write(f"**Progress Level:** {topic_data['RAG_Progress']}")
st.write(f"**Recommendation:** {topic_data['Recommendation_Action']}")

# Encouragement messages
encouragements = {
    "🟢 Green": [
        "You're doing awesome! Keep going! 🌟",
        "Way to go! You're a CNA star! 💪"
    ],
    "🟡 Amber": [
        "You're on the right path — keep practicing! 💡",
        "Almost there! A little review will help you shine! ✨"
    ],
    "🔴 Red": [
        "Don't give up! Ask for help and review this topic. ❤️",
        "You're capable of great things — one step at a time! 🙌"
    ]
}
st.markdown("---")
st.subheader("💬 Encouragement")
st.info(random.choice(encouragements[topic_data["RAG_Progress"]]))
