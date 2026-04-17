import streamlit as st
from groq import Groq

st.set_page_config(page_title="CloudPath AI", page_icon="🌐", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

.stApp { background-color: #0a0f1e !important; }
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    background-color: #0a0f1e !important;
    color: #F5F5F0 !important;
}
.block-container { padding: 2rem 2rem !important; max-width: 760px !important; background-color: #0a0f1e !important; }
p { color: #F5F5F0 !important; }
span { color: #F5F5F0 !important; }
label { color: #F5F5F0 !important; }

.hero-header {
    background: linear-gradient(135deg, #0d1526 0%, #162032 100%);
    border: 1px solid #2a3f5f;
    border-top: 3px solid #1D9E75;
    border-radius: 16px;
    padding: 36px 40px;
    margin-bottom: 28px;
    text-align: center;
}
.hero-title { font-family: 'Space Grotesk', sans-serif !important; font-size: 2.6rem !important; font-weight: 700 !important; color: #FFFFFF !important; margin: 8px 0 10px 0 !important; letter-spacing: -0.5px !important; }
.hero-subtitle { font-size: 0.8rem !important; color: #1D9E75 !important; font-weight: 600 !important; margin: 0 0 8px 0 !important; letter-spacing: 2px !important; text-transform: uppercase !important; }
.hero-tagline { font-size: 0.95rem !important; color: #94A3B8 !important; margin: 0 !important; }

.q-wrap { background: #0d1526; border: 1px solid #2a3f5f; border-radius: 12px; padding: 20px 24px 16px 24px; margin-bottom: 12px; }
.q-label { font-size: 0.72rem !important; font-weight: 700 !important; color: #1D9E75 !important; text-transform: uppercase !important; letter-spacing: 2px !important; margin-bottom: 4px !important; display: block !important; }
.q-text { font-size: 1.05rem !important; font-weight: 600 !important; color: #FFFFFF !important; margin-bottom: 10px !important; display: block !important; }

div[data-testid="stSelectbox"] > div > div { background-color: #1a2235 !important; border: 1px solid #2a3f5f !important; border-radius: 8px !important; color: #F5F5F0 !important; }
div[data-testid="stSelectbox"] svg { fill: #94A3B8 !important; }
div[data-testid="stMultiSelect"] > div > div { background-color: #1a2235 !important; border: 1px solid #2a3f5f !important; border-radius: 8px !important; color: #F5F5F0 !important; }
span[data-baseweb="tag"] { background-color: #1D9E75 !important; color: #FFFFFF !important; border-radius: 6px !important; }

.stButton > button { background: linear-gradient(135deg, #1D9E75 0%, #0F6E56 100%) !important; color: #FFFFFF !important; border: none !important; border-radius: 10px !important; padding: 14px 32px !important; font-size: 1rem !important; font-weight: 600 !important; width: 100% !important; margin-top: 8px !important; letter-spacing: 0.3px !important; }
.stButton > button:hover { background: linear-gradient(135deg, #22b886 0%, #1D9E75 100%) !important; }

.roadmap-wrap { background: #0d1526 !important; border: 1px solid #1D9E75 !important; border-radius: 16px !important; padding: 28px !important; margin-top: 24px !important; }
.roadmap-heading { font-family: 'Space Grotesk', sans-serif !important; font-size: 1.3rem !important; font-weight: 700 !important; color: #FFFFFF !important; margin-bottom: 20px !important; padding-bottom: 14px !important; border-bottom: 1px solid #1e2d40 !important; }
.r-section { background: #1a2235 !important; border-left: 3px solid #1D9E75 !important; border-radius: 8px !important; padding: 16px 18px !important; margin-bottom: 10px !important; }
.r-title { font-size: 0.72rem !important; font-weight: 700 !important; color: #1D9E75 !important; text-transform: uppercase !important; letter-spacing: 1.5px !important; margin-bottom: 8px !important; }
.r-content { font-size: 0.9rem !important; color: #E2E8F0 !important; line-height: 1.8 !important; }
.success-box { background: #085041 !important; border: 1px solid #1D9E75 !important; border-radius: 8px !important; padding: 12px !important; text-align: center !important; color: #9FE1CB !important; font-size: 0.85rem !important; margin-top: 14px !important; }

.book-call-section {
    background: linear-gradient(135deg, #0d1526 0%, #162032 100%);
    border: 1px solid #C9A84C;
    border-top: 3px solid #C9A84C;
    border-radius: 16px;
    padding: 32px 36px;
    margin-top: 32px;
    text-align: center;
}
.book-call-title {
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.4rem !important;
    font-weight: 700 !important;
    color: #FFFFFF !important;
    margin-bottom: 10px !important;
}
.book-call-subtitle {
    font-size: 0.9rem !important;
    color: #94A3B8 !important;
    margin-bottom: 24px !important;
    line-height: 1.6 !important;
}
.book-call-points {
    display: flex;
    justify-content: center;
    gap: 24px;
    flex-wrap: wrap;
    margin-bottom: 24px;
}
.book-call-point {
    background: #1a2235;
    border: 1px solid #2a3f5f;
    border-radius: 8px;
    padding: 12px 18px;
    font-size: 0.82rem !important;
    color: #E2E8F0 !important;
    min-width: 160px;
}
.book-call-point span {
    color: #C9A84C !important;
    font-weight: 700 !important;
    display: block !important;
    margin-bottom: 4px !important;
    font-size: 0.75rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
}
.calendly-btn {
    display: inline-block;
    background: linear-gradient(135deg, #C9A84C 0%, #a8873d 100%);
    color: #0a0f1e !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    padding: 14px 36px;
    border-radius: 10px;
    text-decoration: none !important;
    letter-spacing: 0.3px;
    transition: all 0.2s ease;
}
.calendly-btn:hover { background: linear-gradient(135deg, #d4b05a 0%, #C9A84C 100%); }
.smk-badge {
    margin-top: 16px;
    font-size: 0.75rem !important;
    color: #4B5563 !important;
}

.footer-text { text-align: center !important; color: #4B5563 !important; font-size: 0.75rem !important; margin-top: 36px !important; padding-top: 16px !important; border-top: 1px solid #1e2d40 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-header">
    <p class="hero-subtitle">🌐 Powered by AI</p>
    <p class="hero-title">CloudPath AI</p>
    <p class="hero-tagline">Answer 5 questions · Get your personalized Cloud & AI career roadmap</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""<div class="q-wrap"><span class="q-label">Question 1 of 5</span><span class="q-text">What is your current role?</span></div>""", unsafe_allow_html=True)
q1 = st.selectbox("q1", ["Student", "Software Developer", "Backend Engineer", "DevOps Engineer", "Data Engineer", "IT Professional", "Career Switcher", "Other"], label_visibility="collapsed")

st.markdown("""<div class="q-wrap"><span class="q-label">Question 2 of 5</span><span class="q-text">What is your experience level?</span></div>""", unsafe_allow_html=True)
q2 = st.selectbox("q2", ["No experience yet", "0-1 years", "1-3 years", "3-5 years", "5+ years"], label_visibility="collapsed")

st.markdown("""<div class="q-wrap"><span class="q-label">Question 3 of 5</span><span class="q-text">Which Cloud & AI areas interest you most?</span></div>""", unsafe_allow_html=True)
q3 = st.multiselect("q3", ["Azure DevOps & CI/CD", "Cloud Security & IAM", "AI Automation & Agents", "Machine Learning & MLOps", "Data Engineering", "Backend & API Development", "Infrastructure as Code", "Monitoring & Observability"], label_visibility="collapsed")

st.markdown("""<div class="q-wrap"><span class="q-label">Question 4 of 5</span><span class="q-text">What is your primary career goal?</span></div>""", unsafe_allow_html=True)
q4 = st.selectbox("q4", ["Get my first cloud job", "Transition into AI/ML", "Get promoted to senior level", "Build my own AI product", "Upskill for current role", "Switch from backend to cloud/DevOps"], label_visibility="collapsed")

st.markdown("""<div class="q-wrap"><span class="q-label">Question 5 of 5</span><span class="q-text">How much time can you dedicate per week?</span></div>""", unsafe_allow_html=True)
q5 = st.selectbox("q5", ["1-2 hours", "3-5 hours", "5-10 hours", "10+ hours"], label_visibility="collapsed")

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
                        <div class="r-title">{icons.get(section, '')} {section}</div>
                        <div class="r-content">{content.strip().replace(chr(10), '<br>')}</div>
                    </div>
                    """, unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('<div class="success-box">✦ Roadmap generated — save this and revisit in 30 days</div>', unsafe_allow_html=True)

st.markdown("""
<div class="book-call-section">
    <p class="book-call-title">✦ Want Personal Guidance?</p>
    <p class="book-call-subtitle">Your roadmap is a starting point. Book a free 30-minute Zoom call with Sai Manasa Karanam for personalized advice on your cloud and AI career path.</p>
    <div class="book-call-points">
        <div class="book-call-point">
            <span>What we cover</span>
            Resume & LinkedIn review
        </div>
        <div class="book-call-point">
            <span>What we cover</span>
            Career transition strategy
        </div>
        <div class="book-call-point">
            <span>What we cover</span>
            Cloud & AI learning plan
        </div>
        <div class="book-call-point">
            <span>Duration</span>
            30 minutes · Free
        </div>
    </div>
    <a href="https://calendly.com/saimanasakaranam/30min" target="_blank" class="calendly-btn">
        📅 Book a Free Zoom Call
    </a>
    <p class="smk-badge">Sai Manasa Karanam · Cloud & AI Engineer · Northeastern University</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="footer-text">Built by Sai Manasa Karanam · Cloud & AI Engineer · Northeastern University · Boston MA</div>', unsafe_allow_html=True)
