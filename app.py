import streamlit as st
from groq import Groq

st.set_page_config(page_title="CloudPath AI", page_icon="🌐", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

* { font-family: 'Inter', sans-serif; }

.main { background-color: #0a0f1e; }
.block-container { padding: 2rem 2rem; max-width: 760px; }

h1, h2, h3 { font-family: 'Space Grotesk', sans-serif !important; }

.hero-header {
    background: linear-gradient(135deg, #0d1526 0%, #162032 100%);
    border: 1px solid #1e2d40;
    border-radius: 16px;
    padding: 36px 40px;
    margin-bottom: 32px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero-header::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #1D9E75, #C9A84C, #1D9E75);
}
.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.4rem;
    font-weight: 700;
    color: #F5F5F0;
    margin: 0 0 8px 0;
    letter-spacing: -0.5px;
}
.hero-subtitle {
    font-size: 1rem;
    color: #1D9E75;
    font-weight: 500;
    margin: 0 0 6px 0;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.hero-tagline {
    font-size: 0.9rem;
    color: #94A3B8;
    margin: 0;
}

.section-card {
    background: linear-gradient(135deg, #0d1526 0%, #111827 100%);
    border: 1px solid #1e2d40;
    border-radius: 12px;
    padding: 28px 32px;
    margin-bottom: 16px;
}
.section-card:hover {
    border-color: #1D9E75;
    transition: border-color 0.3s ease;
}
.question-label {
    font-size: 0.75rem;
    font-weight: 600;
    color: #1D9E75;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 8px;
    display: block;
}
.question-text {
    font-size: 1rem;
    font-weight: 600;
    color: #F5F5F0;
    margin-bottom: 12px;
}

div[data-testid="stSelectbox"] > div > div {
    background-color: #1a2235 !important;
    border: 1px solid #1e2d40 !important;
    border-radius: 8px !important;
    color: #F5F5F0 !important;
    font-size: 0.9rem !important;
}
div[data-testid="stSelectbox"] > div > div:hover {
    border-color: #1D9E75 !important;
}
div[data-testid="stMultiSelect"] > div > div {
    background-color: #1a2235 !important;
    border: 1px solid #1e2d40 !important;
    border-radius: 8px !important;
    color: #F5F5F0 !important;
}
span[data-baseweb="tag"] {
    background-color: #1D9E75 !important;
    color: #F5F5F0 !important;
    border-radius: 6px !important;
}

.stButton > button {
    background: linear-gradient(135deg, #1D9E75 0%, #0F6E56 100%) !important;
    color: #F5F5F0 !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 14px 32px !important;
    font-size: 1rem !important;
    font-weight: 600 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    width: 100% !important;
    letter-spacing: 0.5px !important;
    transition: all 0.3s ease !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #22b886 0%, #1D9E75 100%) !important;
    transform: translateY(-1px) !important;
}

.roadmap-container {
    background: linear-gradient(135deg, #0d1526 0%, #111827 100%);
    border: 1px solid #1D9E75;
    border-radius: 16px;
    padding: 32px;
    margin-top: 24px;
}
.roadmap-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: #F5F5F0;
    margin-bottom: 20px;
    padding-bottom: 16px;
    border-bottom: 1px solid #1e2d40;
}
.roadmap-section {
    background: #1a2235;
    border-radius: 10px;
    padding: 18px 20px;
    margin-bottom: 12px;
    border-left: 3px solid #1D9E75;
}
.roadmap-section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.8rem;
    font-weight: 700;
    color: #1D9E75;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 8px;
}
.roadmap-section-content {
    font-size: 0.9rem;
    color: #E2E8F0;
    line-height: 1.8;
}

.success-banner {
    background: linear-gradient(135deg, #085041 0%, #0F6E56 100%);
    border: 1px solid #1D9E75;
    border-radius: 10px;
    padding: 14px 20px;
    text-align: center;
    margin-top: 16px;
    color: #9FE1CB;
    font-size: 0.9rem;
    font-weight: 500;
}

.footer {
    text-align: center;
    color: #4B5563;
    font-size: 0.75rem;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #1e2d40;
}

.divider {
    border: none;
    border-top: 1px solid #1e2d40;
    margin: 24px 0;
}

.stSpinner > div {
    border-top-color: #1D9E75 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-header">
    <p class="hero-subtitle">🌐 Powered by AI</p>
    <h1 class="hero-title">CloudPath AI</h1>
    <p class="hero-tagline">Answer 5 questions · Get your personalized Cloud & AI career roadmap</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<span class="question-label">Question 1 of 5</span>', unsafe_allow_html=True)
st.markdown('<p class="question-text">What is your current role?</p>', unsafe_allow_html=True)
q1 = st.selectbox("", ["Student", "Software Developer", "Backend Engineer", "DevOps Engineer", "Data Engineer", "IT Professional", "Career Switcher", "Other"], key="q1", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<span class="question-label">Question 2 of 5</span>', unsafe_allow_html=True)
st.markdown('<p class="question-text">What is your experience level?</p>', unsafe_allow_html=True)
q2 = st.selectbox("", ["No experience yet", "0-1 years", "1-3 years", "3-5 years", "5+ years"], key="q2", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<span class="question-label">Question 3 of 5</span>', unsafe_allow_html=True)
st.markdown('<p class="question-text">Which Cloud & AI areas interest you most?</p>', unsafe_allow_html=True)
q3 = st.multiselect("", ["Azure DevOps & CI/CD", "Cloud Security & IAM", "AI Automation & Agents", "Machine Learning & MLOps", "Data Engineering", "Backend & API Development", "Infrastructure as Code", "Monitoring & Observability"], key="q3", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<span class="question-label">Question 4 of 5</span>', unsafe_allow_html=True)
st.markdown('<p class="question-text">What is your primary career goal?</p>', unsafe_allow_html=True)
q4 = st.selectbox("", ["Get my first cloud job", "Transition into AI/ML", "Get promoted to senior level", "Build my own AI product", "Upskill for current role", "Switch from backend to cloud/DevOps"], key="q4", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<span class="question-label">Question 5 of 5</span>', unsafe_allow_html=True)
st.markdown('<p class="question-text">How much time can you dedicate per week?</p>', unsafe_allow_html=True)
q5 = st.selectbox("", ["1-2 hours", "3-5 hours", "5-10 hours", "10+ hours"], key="q5", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

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

            st.markdown('<div class="roadmap-container">', unsafe_allow_html=True)
            st.markdown('<div class="roadmap-title">🗺 Your Personalized CloudPath Roadmap</div>', unsafe_allow_html=True)

            icons = {
                "WHERE YOU ARE NOW": "📍",
                "YOUR 30-DAY QUICK WINS": "⚡",
                "YOUR 90-DAY MILESTONES": "🎯",
                "YOUR 6-MONTH GOAL": "🚀",
                "RECOMMENDED RESOURCES": "📚",
                "YOUR NEXT SINGLE STEP": "✦"
            }

            for section, content in sections.items():
                if content.strip():
                    st.markdown(f"""
                    <div class="roadmap-section">
                        <div class="roadmap-section-title">{icons.get(section,'')} {section}</div>
                        <div class="roadmap-section-content">{content.strip().replace(chr(10), '<br>')}</div>
                    </div>
                    """, unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('<div class="success-banner">✦ Roadmap generated — save this and revisit in 30 days</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    Built by Sai Manasa Karanam · Cloud & AI Engineer · Northeastern University · Boston MA
</div>
""", unsafe_allow_html=True)
