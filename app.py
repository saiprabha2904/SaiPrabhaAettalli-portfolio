import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="Sai Prabha Aettalli - Senior AI Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load external CSS
def load_css(file_path):
    """Load CSS from external file"""
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            css_content = f.read()
        st.markdown(f'<style>{css_content}</style>', unsafe_allow_html=True)
    else:
        st.error(f"CSS file not found: {file_path}")

# Load the styles
load_css('styles.css')

# Navigation Bar
import base64
# Function to load and encode image
def get_image_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# Try to load profile image
profile_img_base64 = get_image_base64("profile.jpg")
if not profile_img_base64:
    profile_img_base64 = get_image_base64("assets/profile.jpg")


# Create navigation bar with profile
if profile_img_base64:
    st.markdown("""
    <div class="nav-bar">
        <div class="nav-profile">
            <div class="nav-profile-name">Sai Prabha Aettalli</div>
        </div>
        <div class="nav-links">
            <a href="#home" class="nav-link">🏠 Home</a>
            <a href="#profile" class="nav-link">💼 Profile</a>
            <a href="#achievements" class="nav-link">🏆 Achievements</a>
            <a href="#experience" class="nav-link">💼 Experience</a>
            <a href="#skills" class="nav-link">🛠️ Skills</a>
            <a href="#certifications" class="nav-link">🎓 Certifications</a>
            <a href="#education" class="nav-link">🎓 Education</a>
            <a href="#contact" class="nav-link">📞 Contact</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    # Fallback without image
    st.markdown("""
    <div class="nav-bar">
        <div class="nav-profile">
            <div class="nav-profile-name">Sai Prabha Aettalli</div>
        </div>
        <div class="nav-links">
            <a href="#home" class="nav-link">🏠 Home</a>
            <a href="#profile" class="nav-link">💼 Profile</a>
            <a href="#achievements" class="nav-link">🏆 Achievements</a>
            <a href="#experience" class="nav-link">💼 Experience</a>
            <a href="#skills" class="nav-link">🛠️ Skills</a>
            <a href="#certifications" class="nav-link">🎓 Certifications</a>
            <a href="#education" class="nav-link">🎓 Education</a>
            <a href="#contact" class="nav-link">📞 Contact</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Hero Section
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

# Display hero section with profile image if available
if profile_img_base64:
    st.markdown(f"""
    <div class="hero-section">
        <img src="data:image/jpeg;base64,{profile_img_base64}" class="hero-profile-img" style="width: 200px; height: 250px; border-radius: 10px; border: 5px solid #2E86AB; object-fit: cover; margin-bottom: 20px; box-shadow: 0 8px 25px rgba(46, 134, 171, 0.5);" alt="Sai Prabha Aettalli">
        <h2 class="stylish-name" style="color: #9ca3af !important; -webkit-text-fill-color: #9ca3af !important;">Sai Prabha Aettalli</h2>
        <p class="hero-subtitle" style="margin-top: 0; margin-bottom: 25px;">Senior AI Engineer | Agentic AI & LLM Systems | Automation | Data Engineering | RPA</p>
        <div class="hero-buttons">
            <a href="#experience" class="hero-btn hero-btn-primary">
                🚀 View Experience
            </a>
            <a href="#contact" class="hero-btn hero-btn-secondary">
                📧 Get in Touch
            </a>
        </div>
        <p class="hero-location" style="font-size: 1.1em; color: #a0a0a0; margin-top: 25px;">🇬🇧 United Kingdom</p>
        <div class="hero-visa-badge" style="display: inline-block; background: linear-gradient(135deg, rgba(46, 134, 171, 0.3) 0%, rgba(241, 143, 1, 0.3) 100%); padding: 10px 20px; border-radius: 20px; border: 2px solid #2E86AB; margin-top: 15px;">
            <p style="font-size: 1em; color: #c9a86a; font-weight: 600; margin: 0;">✅ Eligible to work in the UK · No sponsorship required</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="hero-section">
        <h1 class="hero-title">Sai Prabha Aettalli</h1>
        <p class="hero-subtitle">Senior AI Engineer · Agentic AI & LLM Systems · Automation</p>
        <div class="hero-buttons">
            <a href="#experience" class="hero-btn hero-btn-primary">
                🚀 View Experience
            </a>
            <a href="#contact" class="hero-btn hero-btn-secondary">
                📧 Get in Touch
            </a>
        </div>
        <p style="font-size: 1.1em; color: #a0a0a0; margin-top: 25px;">🇬🇧 United Kingdom</p>
        <div style="display: inline-block; background: linear-gradient(135deg, rgba(46, 134, 171, 0.3) 0%, rgba(241, 143, 1, 0.3) 100%); padding: 10px 20px; border-radius: 20px; border: 2px solid #2E86AB; margin-top: 15px;">
            <p style="font-size: 1em; color: #c9a86a; font-weight: 600; margin: 0;">✅ Eligible to work in the UK · No sponsorship required</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Professional Profile
st.markdown('<div id="profile" class="section-spacer"></div>', unsafe_allow_html=True)
st.header("💼 Professional Profile")
st.markdown("""
Results-driven Senior AI Engineer with **9+ years of experience** designing and delivering enterprise-grade
LLM, agentic AI, RPA and automation solutions across banking, insurance and enterprise software sectors.
Specialist in **IBM Watson Orchestrate, IBM ADK, LangGraph and LangChain**, with a proven track record
of translating complex business requirements into scalable, production-ready cloud-based AI and automation systems.

Experienced in architecting end-to-end data pipelines using **Azure Data Factory** integrated with
IBM Watson Orchestrate and BAW, enabling intelligent straight-through processing across enterprise workflows.
Skilled at leading cross-functional collaboration between technical and business stakeholders to drive measurable
operational efficiency.
""")

# Key Achievements
st.markdown('<div id="achievements" class="section-spacer"></div>', unsafe_allow_html=True)
st.header("🏆 Key Achievements")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="achievement-card">
        <div class="achievement-number">60%</div>
        <div class="achievement-text">Reduction in data preparation time through ADF pipeline integration</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="achievement-card">
        <div class="achievement-number">65%</div>
        <div class="achievement-text">Reduction in manual processing time for CitiBank workflows</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="achievement-card">
        <div class="achievement-number">4+ hrs</div>
        <div class="achievement-text">Saved per case through touchless workflow automation</div>
    </div>
    """, unsafe_allow_html=True)

# Professional Experience
st.markdown('<div id="experience" class="section-spacer"></div>', unsafe_allow_html=True)
st.header("💼 Professional Experience")

# IBM
with st.expander("🏢 **IBM** - Software Engineer (Agentic AI, Generative AI & Automation) | Jan 2025 – Present", expanded=True):
    st.markdown("**📅 January 2025 – Present | Hyderabad, India**")
    
    st.subheader("Agentic AI & Generative AI - Watson Orchestrate & IBM ADK")
    st.markdown("""
    - Designed and deployed **LLM-powered AI agents**, skills and tools on IBM Watson Orchestrate, enabling intelligent autonomous task execution across 10+ enterprise workflows
    - Built and configured **MCP (Model Context Protocol) servers** and tools, reducing integration effort by ~30%
    - Engineered **multi-agent orchestration pipelines** in IBM ADK with dynamic agent-to-agent communication
    - Built fully functional Generative AI systems using **LangGraph** implementing sequential chains, cyclic stateful graphs with persistent memory
    - Applied advanced LLM reasoning strategies including **ReAct, Plan-and-Execute and Tool-Augmented Reasoning**
    """)
    
    st.subheader("Data Engineering - ADF, Watson Orchestrate & BAW Integration")
    st.markdown("""
    - Architected **Azure Data Factory (ADF) pipelines** ingesting data from 5+ heterogeneous sources
    - Engineered seamless data handoff between ADF and Watson Orchestrate, reducing data preparation overhead by ~60%
    - Deployed **PySpark-based data formatting** in Databricks, reducing infrastructure costs by 40%
    """)

# LTIMindtree
with st.expander("🏢 **LTIMindtree** - Senior Specialist (RPA & Hyperautomation) | Nov 2022 – Jan 2025"):
    st.markdown("**📅 November 2022 – January 2025 | Hyderabad, India**")
    st.markdown("**Client: CitiBank Retail Services**")
    st.markdown("""
    - Designed and deployed **8+ production bots** using Automation Anywhere A360, reducing manual processing time by 65%
    - Led end-to-end **hyperautomation pipeline architecture** integrating Xceptor with A360 bots
    - Managed **CI/CD bot deployment pipeline** via Jenkins, Bitbucket and RLM with zero production rollback incidents
    - Built **Tableau dashboards** for bot performance metrics, informing cost-saving decisions exceeding £150,000 per annum
    - Implemented robust exception handling ensuring graceful degradation and uninterrupted straight-through processing
    """)

# First American
with st.expander("🏢 **First American** - Senior Software Engineer (Intelligent Automation) | Jun 2020 – Nov 2022"):
    st.markdown("**📅 June 2020 – November 2022 | Hyderabad, India**")
    st.markdown("**Mortgage Solutions Business**")
    st.markdown("""
    - Designed and deployed **10+ production-grade bots** automating end-to-end mortgage processes, reducing errors by 80%
    - Led end-to-end **migration from AA v11 to A360** with zero business disruption
    - Integrated **Power BI and Elasticsearch** for real-time bot monitoring, reducing MTTR by 50%
    - Managed full bot lifecycle using **Azure DevOps** for sprint tracking and release coordination
    """)

# Cambridge Enterprise Technologies
with st.expander("🏢 **Cambridge Enterprise Technologies** - Senior Engineer (IDP) | Sep 2019 – May 2020"):
    st.markdown("**📅 September 2019 – May 2020 | Hyderabad, India**")
    st.markdown("**Client: Hill's Pet Nutrition**")
    st.markdown("""
    - Architected end-to-end **intelligent document processing pipeline** using IQ Bot, achieving 95%+ extraction accuracy
    - Built Task Bots in A360 for post-extraction workflow, enabling fully touchless end-to-end processing
    - Successfully automated four business cases; developed POCs securing stakeholder approval
    """)

# Kantar
with st.expander("🏢 **Kantar** - Senior Analyst (Automation & Data Processing) | Jun 2016 – Sep 2019"):
    st.markdown("**📅 June 2016 – September 2019 | Hyderabad, India**")
    st.markdown("**Clients: New York Life Insurance & Unilever (USA)**")
    st.markdown("""
    - Architected end-to-end data processing automation reducing 4+ hour manual process to single-click touchless workflow
    - Designed **reusable Meta Bot library**, reducing development time by 40%
    - Built centralised exception handling framework with automated email alerts and RCA reports
    - 🏆 Awarded **Kantar Operations Performance Award (KOPA) 2018**
    """)

# Core Skills
st.markdown('<div id="skills" class="section-spacer"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="skills-wrapper">
    <h2 style="color: #2E86AB; margin-bottom: 15px; font-size: 1.5em;">🛠️ Core Skills</h2>
""", unsafe_allow_html=True)

skills_data = {
    "🤖 Agentic & Generative AI": [
        "IBM Watson Orchestrate", "IBM ADK", "LangGraph", "LangChain",
        "MCP Servers & Tools", "AI Assistant Builder", "IBM BOB"
    ],
    "💻 Programming Languages": [
        "Python", "SQL", "JavaScript", "PowerShell", "VBScript"
    ],
    "🧠 LLM Techniques": [
        "LLM Reasoning", "RAG", "Prompt Engineering", "ReAct",
        "Plan-and-Execute", "Tool-Augmented Reasoning", "Multi-Agent Orchestration"
    ],
    "📈 Analytics & Monitoring": [
        "Tableau", "Power BI", "Elasticsearch"
    ],
    "🔄 RPA & Automation": [
        "Automation Anywhere A360/v11", "IQ Bot", "UiPath",
        "Power Automate", "Blue Prism", "Xceptor", "Intelligent Document Processing"
    ],
    "🗄️ Databases": [
        "Oracle DB", "PostgreSQL", "SQL Server", "MySQL", "IBM DB2"
    ],
    "📊 Data Engineering": [
        "Azure Data Factory (ADF)", "Databricks", "PySpark",
        "ETL Pipelines", "Data Ingestion", "Transformation & Cleansing"
    ],
    "🌐 Web & Integration": [
        "RESTful APIs", "JSON", "XML", "SOAP", "Webhooks", "Swagger/OpenAPI", "HTML5"
    ],
    "⚙️ Business Process Automation": [
        "IBM BAW (Business Automation Workflow)", "Watson Orchestrate Integration",
        "Coach UI", "Process Services", "REST Services"
    ],
    "🤝 Collaboration & ITSM": [
        "Jira", "Confluence", "ServiceNow", "Notion",
        "Microsoft Teams", "Slack", "SharePoint Online"
    ],
    "☁️ Cloud & DevOps": [
        "IBM Cloud Pak", "Azure", "Azure DevOps", "Jenkins CI/CD",
        "Git", "GitHub", "GitLab", "Bitbucket", "RLM"
    ],
    "🪟 Microsoft Stack": [
        "Power Platform", "Azure Active Directory (Entra ID)",
        "SharePoint Online", "Visio", "Azure DevOps"
    ]
}

for category, skills in skills_data.items():
    skills_html = "".join([f'<span class="skill-badge">{skill}</span>' for skill in skills])
    st.markdown(f"""
    <div class="skills-category">
        <div class="skills-category-title">{category}</div>
        <div>{skills_html}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Certifications
st.markdown('<div id="certifications" class="section-spacer"></div>', unsafe_allow_html=True)
st.header("🎓 Certifications")

certifications = [
    ("IBM watsonx: Technical Essentials", "IBM", "August 2025"),
    ("IBM watsonx Orchestrate: Getting Started with Automation Builder", "IBM", "February 2025"),
    ("Python for Data Science", "Simplilearn", "December 2023"),
    ("Automation Anywhere Certified Advanced RPA Professional (Automation 360)", "Automation Anywhere", "August 2022"),
    ("IQ Bot Developer", "Automation Anywhere", "September 2019"),
    ("Automation Anywhere Certified Advanced RPA Professional (V11.0)", "Automation Anywhere", "April 2019")
]

for cert, org, date in certifications:
    st.markdown(f"""
    <div class="cert-card">
        <div class="cert-title">{cert}</div>
        <div class="cert-details">🏛️ {org} | 📅 {date}</div>
    </div>
    """, unsafe_allow_html=True)

# Education
st.markdown('<div id="education" class="section-spacer"></div>', unsafe_allow_html=True)
st.header("🎓 Education")
st.markdown("""
<div class="education-card">
    <div class="education-degree">Bachelor of Technology (B.Tech)</div>
    <div class="education-field">Electronics & Communications Engineering</div>
    <div class="education-details">
        🎓 <strong>JB Institute of Engineering and Technology</strong>, Hyderabad, India<br>
        📅 <strong>2012 – 2016</strong><br>
        🏆 <strong>First Class: 79.2%</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# Contact Information
st.markdown('<div id="contact" class="section-spacer"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="contact-hero">
    <h2 class="contact-title">📞 Let's Connect</h2>
    <p style="font-size: 1.05em; color: #a0a0a0; margin-bottom: 20px;">
        Open to discussing new opportunities and collaborations!
    </p>
    <div class="contact-grid">
        <div class="contact-card">
            <span class="contact-icon">📧</span>
            <div class="contact-label">Email</div>
            <div class="contact-value">
                <a href="mailto:saiprabha2904@gmail.com">saiprabha2904@gmail.com</a>
            </div>
        </div>
        <div class="contact-card">
            <span class="contact-icon">💼</span>
            <div class="contact-label">LinkedIn</div>
            <div class="contact-value">
                <a href="https://linkedin.com/in/saiprabha29" target="_blank">linkedin.com/in/saiprabha29</a>
            </div>
        </div>
        <div class="contact-card">
            <span class="contact-icon">🇬🇧</span>
            <div class="contact-label">Location</div>
            <div class="contact-value">United Kingdom</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #a0a0a0; padding: 20px;">
    <p>© 2026 Sai Prabha Aettalli | Senior AI Engineer</p>
</div>
""", unsafe_allow_html=True)

# Made with Bob
