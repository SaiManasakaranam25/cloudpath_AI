import streamlit as st
import anthropic

st.set_page_config(page_title="CloudPath AI", page_icon="🌐", layout="centered")

st.markdown("""
<style>
.main { background-color: #1a1730; }
h1 { color: #EEEDFE; }
h2, h3 { color: #9FE1CB; }
p, li { color: #CECBF6; }
.stButton>button {
    background-color: #1D9E75;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 24px;
    font-size: 16px;
}
.stButton>button:hover { background-color: #0F6E56; }
</style>
""", unsafe_allow_html=True)

st.markdown("## 🌐 CloudPath AI")
st.markdown("#### Your personalized Cloud & AI career roadmap generator")
st.markdown("---")

st.markdown("### Tell me about yourself")

q1 = st.selectbox(
    "1. What is your current role?",
    ["Student", "Software Developer", "Backend Engineer", "DevOps Engineer", "Data Engineer", "IT Professional", "Career Switcher", "Other"]
)

q2 = st.selectbox(
    "2. What is your experience level?",
    ["No experience yet", "0-1 years", "1-3 years", "3-5 years", "5+ years"]
)

q3 = st.multiselect(
    "3. Which cloud/AI areas interest you most? (select all that apply)",
    ["Azure DevOps & CI/CD", "Cloud Security & IAM", "AI Automation & Agents", "Machine Learning & MLOps", "Data Engineering", "Backend & API Development", "Infrastructure as Code", "Monitoring & Observability"]
)

q4 = st.selectbox(
    "4. What is your primary goal?",
    ["Get my first cloud job", "Transition into AI/ML", "Get promoted to senior level", "Build my own AI product", "Upskill for current role", "Switch from backend to cloud/DevOps"]
)

q5 = st.selectbox(
    "5. How much time can you dedicate per week?",
    ["1-2 hours", "3-5 hours", "5-10 hours", "10+ hours"]
)

st.markdown("---")

if st.button("Generate My Roadmap"):
    if not q3:
        st.warning("Please select at least one area of interest in question 3.")
    else:
        with st.spinner("Building your personalized roadmap..."):
            client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
            
            prompt = f"""You are CloudPath AI, a career advisor specializing in Cloud and AI engineering careers.

A user has answered 5 questions about their background:
1. Current role: {q1}
2. Experience level: {q2}
3. Areas of interest: {', '.join(q3)}
4. Primary goal: {q4}
5. Time available per week: {q5}

Generate a personalized Cloud and AI career roadmap for them. Structure your response as:

**Your CloudPath Roadmap**

**Where You Are Now**
(2-3 sentences about their current position)

**Your 30-Day Quick Wins**
(3-4 specific actionable steps they can do right now)

**Your 90-Day Milestones**
(3-4 concrete milestones to hit in 3 months)

**Your 6-Month Goal**
(What they should be able to do or achieve in 6 months)

**Recommended Resources**
(3-4 specific courses, certifications, or tools relevant to their interests)

**Your Next Single Step**
(One clear action they should take today)

Be specific, encouraging, and practical. Reference their specific interests and goals throughout."""

            message = client.messages.create(
                model="claude-haiku-4-5",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            
            st.markdown("### Your Personalized Roadmap")
            st.markdown(message.content[0].text)
            st.success("Roadmap generated! Save this and revisit it in 30 days.")

st.markdown("---")
st.markdown("<p style='text-align:center; color:#534AB7; font-size:12px;'>Built by Sai Manasa Karanam · Cloud & AI Engineer · Northeastern University</p>", unsafe_allow_html=True)
