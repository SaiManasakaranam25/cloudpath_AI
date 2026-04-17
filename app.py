import streamlit as st
from groq import Groq

st.set_page_config(page_title="CloudPath AI", page_icon="🌐", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0a0f1e;
    color: #F5F5F0;
}
.block-container { padding: 2rem 2rem; max-width: 760px; }

.hero-header {
    background: linear-gradient(135deg, #0d1526 0%, #162032 100%);
    border: 1px solid #2a3f5f;
    border-top: 3px solid #1D9E75;
    border-radius: 16px;
    padding: 36px 40px;
    margin-bottom: 28px;
    text-align: center;
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.6rem;
    font-weight: 700;
    color: #FFFFFF;
    margin: 8px 0 10px 0;
    letter-spacing: -0.5px;
}
.hero-subtitle {
    font-size: 0.8rem;
    color: #1D9E75;
    font-weight: 600;
    margin: 0 0 8px 0;
    letter-spacing: 2px;
    text-transform: uppercase;
}
.hero-tagline {
    font-size: 0.95rem;
    color: #94A3B8;
    margin: 0;
}

.q-label {
    font-size: 0.72rem;
    font-weight: 700;
    color: #1D9E75;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 4px;
    margin-top: 20px;
    display: block;
}
.q-text {
    font-size: 1rem;
    font-weight: 600;
    color: #FFFFFF;
    margin-bottom: 6px;
    display: block;
}

div[data-testid="stSelectbox"] > div > div {
    background-color: #1a2235 !important;
    border: 1px solid #2a3f5f !important;
    border-radius: 8px !important;
    color: #F5F5F0 !important;
}
div[data-testid="stMultiSelect"] > div > div {
    background-color: #1a2235 !important;
    border: 1px solid #2a3f5f !important;
    border-radius: 8px !important;
    color: #F5F5F0 !important;
}
span[data-baseweb="tag"] {
    background-color: #1D9E75 !important;
    color: #FFFFFF !important;
    border-radius: 6px !important;
}

.stButton > button {
    background: linear-gradient(135deg, #1D9E75 0%, #0F6E56 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 14px 32px !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    width: 100% !important;
    margin-top: 16px !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #22b886 0%, #1D9E75 100%) !important;
}

.roadmap-wrap {
    background: #0d1526;
    border: 1px solid #1D9E75;
    border-radius: 16px;
    padding: 28px;
    margin-top: 24px;
}
.roadmap-heading {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #FFFFFF;
    margin-bottom: 20px;
    padding-bottom: 14px;
    border-bottom: 1px solid #1e2d40;
}
.r-section {
    background: #1a2235;
    border-left: 3px solid #1D9E75;
    border-radius: 8px;
    padding: 16px 18px;
    margin-bottom: 10px;
}
.r-title {
    font-size: 0.72rem;
    font-weight: 700;
    color: #1D9E75;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 8px;
}
.r-content {
    font-size: 0.9rem;
    color: #E2E8F0;
    line-height: 1.8;
}
.success-box {
    background: #085041;
    border: 1px solid #1D9E75;
    border-radius: 8px;
    padding: 12px;
    text-align: center;
    color: #9FE1CB;
    font-size: 0.85rem;
    margin-top: 14px;
}
.footer-text {
    text-align: center;
    color: #4B5563;
    font-size: 0.75rem;
    margin-top: 36px;
    padding-top: 16px;
    border-top: 1px solid #1e2d40;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-header">
    <p class="hero-subtitle">🌐 Powered by AI</p>
    <p class="hero-title">CloudPath AI</p>
    <p class="hero-tagline">Answer 5 questions · Get your personalized Cloud & AI career roadmap</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<span class="q-label">Question 1 of 5</span><span class="q-text">What is your current role?</span>', unsafe_allow_html=True)
q1 = st.selectbox("q1", ["Student", "Software Developer", "Backend Engineer", "DevOps Engineer", "Data Engineer", "IT Professional", "Career Switcher", "Other"], label_visibility="collapsed")

st.markdown('<span class="q-label">Question 2 of 5</span><span class="q-text">What is your experience level?</span>', unsafe_allow_html=True)
q2 = st.selectbox("q2", ["No experience yet", "0-1 years", "1-3 years", "3-5 years", "5+ years"], label_visibility="collapsed")

st.markdown('<span class="q-label">Question 3 of 5</span><span class="q-text">Which Cloud & AI areas interest you most?</span>', unsafe_allow_html=True)
q3 = st.multiselect("q3", ["Azure DevOps & CI/CD", "Cloud Security & IAM", "AI Automation & Agents", "Machine Learning & MLOps", "Data Engineering", "Backend & API Development", "Infrastructure as Code", "Monitoring & Observability"], label_visibility="collapsed")

st.markdown('<span class="q-label">Question 4 of 5</span><span class="q-text">What is your primary career goal?</span>', unsafe_allow_html=True)
q4 = st.selectbox("q4", ["Get my first cloud job", "Transition into AI/ML", "Get promoted to senior level", "Build my own AI product", "Upskill for current role", "Switch from backend to cloud/DevOps"], label_visibility="collapsed")

st.markdown('<span class="q-label">Question 5 of 5</span><span class="q-text">How much time can you dedicate per week?</span>', unsafe_allow_html=True)
q5 = st.selectbox("q5", ["1-2 hours", "3-5 hours", "5-10 hours", "10+ hours"], label_visibility="collapsed")

if st.button("✦ Generate My CloudPath Roadmap"):
    if not q3:
        st.warning("Please select at least one area of interest in Question 3.")
    else:
        with st.spinner("Building your personalized roadmap..."):
            client = Groq(api_key=st.secrets["GROQ_API_KEY"])
            prompt = f"""You are CloudPath AI, a career advisor specializing in Cloud and AI engineering careers.

A user has answered 5 questions:
1. Current role: {q1}
2. Experience level: {q2}
3. Areas of interest: {', '.join(q3)}
4. Primary goal: {q4}
5. Time available per week: {q5}

Generate a personalized Cloud and AI career roadmap. Use EXACTLY these section headers on their own line in ALL CAPS:

WHERE YOU ARE NOW
YOUR 30-DAY QUICK WINS
YOUR 90-DAY MILESTONES
YOUR 6-MONTH GOAL
RECOMMENDED RESOURCES
YOUR NEXT SINGLE STEP

Under each header write the content. Be specific, encouraging, and practical."""

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1200
            )

            raw = response.choices[0].message.content
            sections = {
                "WHERE YOU ARE NOW": "",
                "YOUR 30-DAY QUICK WINS": "",
                "YOUR 90-DAY MILESTONES": "",
                "YOUR 6-MONTH GOAL": "",
                "RECOMMENDED RESOURCES": "",
                "YOUR NEXT SINGLE STEP": ""
            }

            current = None
            for line in raw.split("\n"):
                matched = False
                for key in sections:
                    if key in line.upper():
                        current = key
                        matched = True
                        break
                if not matched and current:
                    sections[current] += line + "\n"

            icons = {
                "WHERE YOU ARE NOW": "📍",
                "YOUR 30-DAY QUICK WINS": "⚡",
                "YOUR 90-DAY MILESTONES": "🎯",
                "YOUR 6-MONTH GOAL": "🚀",
                "RECOMMENDED RESOURCES": "📚",
                "YOUR NEXT SINGLE STEP": "✦"
            }

            st.markdown('<div class="roadmap-wrap">', unsafe_allow_html=True)
            st.markdown('<div class="roadmap-heading">🗺 Your Personalized CloudPath Roadmap</div>', unsafe_allow_html=True)

            for section, content in sections.items():
                if content.strip():
                    st.markdown(f"""
                    <div class="r-section">
                        <div class="r-title">{icons.get(section,'')} {section}</div>
                        <div class="r-content">{content.strip().replace(chr(10), '<br>')}</div>
                    </div>
                    """, unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('<div class="success-box">✦ Roadmap generated — save this and revisit in 30 days</div>', unsafe_allow_html=True)

st.markdown('<div class="footer-text">Built by Sai Manasa Karanam · Cloud & AI Engineer · Northeastern University · Boston MA</div>', unsafe_allow_html=True)
