import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="Sai Prabha Aettalli - Senior AI Engineer",
    page_icon="🤖",
    layout="centered",
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
        width: 50px;
        height: 50px;
        border-radius: 50%;
        border: 3px solid #2E86AB;
        object-fit: cover;
        box-shadow: 0 4px 10px rgba(46, 134, 171, 0.4);
        transition: all 0.3s ease;
    }
    
    .nav-profile-img:hover {
        border-color: #F18F01;
        transform: scale(1.1);
        box-shadow: 0 6px 15px rgba(241, 143, 1, 0.5);
    }
    
    .nav-profile-name {
        font-size: 1.3em;
        font-weight: 700;
        background: linear-gradient(135deg, #2E86AB 0%, #F18F01 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        white-space: nowrap;
    }
    
    .nav-links {
        display: flex;
        justify-content: flex-end;
        flex-wrap: wrap;
        gap: 10px;
        flex: 1;
    }
    
    .nav-link {
        display: inline-block;
        padding: 10px 20px;
        background: rgba(46, 134, 171, 0.2);
        color: #e4e4e4;
        text-decoration: none;
        border-radius: 25px;
        border: 1px solid #2E86AB;
        transition: all 0.3s ease;
        font-weight: 500;
        font-size: 0.95em;
    }
    
    .nav-link:hover {
        background: rgba(241, 143, 1, 0.3);
        border-color: #F18F01;
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(241, 143, 1, 0.3);
        color: #F18F01;
    }
    
    /* Hero section */
    .hero-section {
        text-align: center;
        padding: 30px 20px;
        background: linear-gradient(135deg, rgba(10, 14, 26, 0.95) 0%, rgba(13, 17, 23, 0.95) 100%);
        border-radius: 18px;
        margin-bottom: 25px;
        box-shadow: 0 6px 25px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(46, 134, 171, 0.3);
        position: relative;
        overflow: hidden;
        animation: fadeInUp 1s ease-out;
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(46, 134, 171, 0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }
    
    .hero-section::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent 30%, rgba(241, 143, 1, 0.05) 50%, transparent 70%);
        animation: shimmer 3s ease-in-out infinite;
    }
    
    .hero-section > * {
        position: relative;
        z-index: 1;
    }
    
    .hero-profile-img {
        animation: fadeInScale 1.2s ease-out;
        transition: all 0.4s ease;
    }
    
    .hero-profile-img:hover {
        transform: scale(1.05) rotate(2deg);
        box-shadow: 0 15px 40px rgba(46, 134, 171, 0.6) !important;
    }
    
    .hero-title {
        font-size: 3.5em;
        font-weight: 800;
        background: linear-gradient(135deg, #2E86AB 0%, #A23B72 50%, #F18F01 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        padding: 0;
        animation: fadeInDown 1s ease-out 0.3s both;
    }
    
    .stylish-name {
        font-size: 3em;
        font-weight: 700;
        color: #9ca3af !important;
        margin: 0;
        padding: 0;
        margin-bottom: 15px;
        animation: fadeInDown 1s ease-out 0.3s both;
        letter-spacing: 1px;
        position: relative;
        display: inline-block;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
        text-shadow: none;
    }
    
    .stylish-name::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 50%;
        transform: translateX(-50%);
        width: 60%;
        height: 3px;
        background: linear-gradient(90deg, transparent, #2E86AB, #A23B72, #F18F01, transparent);
        border-radius: 2px;
        animation: breathe 2s ease-in-out infinite;
    }
    
    .stylish-name:hover {
        animation: fadeInDown 1s ease-out 0.3s both, gradientFlow 2s ease infinite;
        transform: scale(1.03);
        transition: transform 0.3s ease;
    }
    
    .hero-subtitle {
        font-size: 1.8em;
        font-weight: 600;
        background: linear-gradient(135deg, #2E86AB 0%, #A23B72 50%, #F18F01 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 200% 200%;
        margin-top: 5px;
        margin-bottom: 30px;
        animation: fadeInUp 1s ease-out 0.5s both, gradientFlow 5s ease infinite;
        text-shadow: 0 2px 10px rgba(46, 134, 171, 0.3);
        letter-spacing: 0.5px;
    }
    
    @keyframes gradientFlow {
        0%, 100% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
    }
    
    .hero-location {
        animation: fadeInUp 1s ease-out 0.7s both;
    }
    
    .hero-visa-badge {
        animation: fadeInUp 1s ease-out 0.9s both, pulse 2s ease-in-out 2s infinite;
    }
    
    /* Hero action buttons */
    .hero-buttons {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: 25px;
        flex-wrap: wrap;
        animation: fadeInUp 1s ease-out 1.1s both;
    }
    
    .hero-btn {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 12px 25px;
        border-radius: 10px;
        font-size: 1em;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.3s ease;
        border: 2px solid;
        cursor: pointer;
    }
    
    .hero-btn-primary {
        /* Dark elegant gradient */
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        color: white;
        border-color: transparent;
        box-shadow: 0 4px 15px rgba(44, 62, 80, 0.5);
    }
    
    .hero-btn-primary:hover {
        background: linear-gradient(135deg, #34495e 0%, #3d566e 100%);
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(44, 62, 80, 0.7);
    }
    
    .hero-btn-secondary {
        background: transparent;
        color: #e4e4e4;
        border-color: rgba(46, 134, 171, 0.5);
        animation: pulse 2s ease-in-out 2s infinite;
    }
    
    .hero-btn-secondary:hover {
        background: rgba(46, 134, 171, 0.2);
        border-color: #2E86AB;
        transform: translateY(-3px);
        box-shadow: 0 4px 15px rgba(46, 134, 171, 0.3);
        animation: none;
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInScale {
        from {
            opacity: 0;
            transform: scale(0.8);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }
    
    @keyframes rotate {
        from {
            transform: rotate(0deg);
        }
        to {
            transform: rotate(360deg);
        }
    }
    
    @keyframes shimmer {
        0%, 100% {
            opacity: 0;
        }
        50% {
            opacity: 1;
        }
    }
    
    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }
    
    /* Achievement cards */
    .achievement-card {
        background: linear-gradient(135deg, rgba(46, 134, 171, 0.2) 0%, rgba(241, 143, 1, 0.2) 100%);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .achievement-card:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 25px rgba(241, 143, 1, 0.3);
    }
    
    .achievement-number {
        font-size: 2.5em;
        font-weight: 800;
        color: #F18F01;
        margin-bottom: 10px;
    }
    
    .achievement-text {
        font-size: 1.1em;
        color: #e4e4e4;
    }
    
    /* Skills section wrapper with animations */
    .skills-wrapper {
        background: linear-gradient(135deg, rgba(30, 60, 114, 0.08) 0%, rgba(42, 82, 152, 0.06) 50%, rgba(30, 60, 114, 0.08) 100%);
        border-radius: 10px;
        padding: 15px 15px;
        margin: 10px 0;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
        border: 1px solid rgba(46, 134, 171, 0.15);
        position: relative;
        overflow: hidden;
        animation: slideInScale 0.8s ease-out;
    }
    
    .skills-wrapper::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(46, 134, 171, 0.1), transparent);
        animation: slideAcross 3s ease-in-out infinite;
    }
    
    .skills-wrapper::after {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #2E86AB, #A23B72, #F18F01, #2E86AB);
        background-size: 300% 300%;
        border-radius: 10px;
        z-index: -1;
        opacity: 0;
        animation: gradientShift 4s ease infinite;
        transition: opacity 0.3s;
    }
    
    .skills-wrapper > * {
        position: relative;
        z-index: 1;
    }
    
    .skills-wrapper:hover {
        border-color: rgba(241, 143, 1, 0.3);
        box-shadow: 0 4px 20px rgba(46, 134, 171, 0.3);
        transform: scale(1.01);
    }
    
    .skills-wrapper:hover::after {
        opacity: 0.3;
    }
    
    @keyframes slideInScale {
        from {
            opacity: 0;
            transform: scale(0.95) translateY(20px);
        }
        to {
            opacity: 1;
            transform: scale(1) translateY(0);
        }
    }
    
    @keyframes slideAcross {
        0% {
            left: -100%;
        }
        50%, 100% {
            left: 100%;
        }
    }
    
    @keyframes gradientShift {
        0%, 100% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
    }
    
    /* Skills category container */
    .skills-category {
        background: linear-gradient(135deg, rgba(46, 134, 171, 0.12) 0%, rgba(162, 59, 114, 0.08) 50%, rgba(241, 143, 1, 0.06) 100%);
        border-radius: 15px;
        padding: 20px 25px;
        margin: 15px 0;
        border: 2px solid rgba(46, 134, 171, 0.4);
        border-left: 5px solid #2E86AB;
        transition: all 0.4s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
        opacity: 0;
        animation: slideInLeft 0.6s ease-out forwards;
        position: relative;
        overflow: hidden;
    }
    
    .skills-category::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.05), transparent);
        transition: left 0.6s;
    }
    
    .skills-category:hover::before {
        left: 100%;
    }
    
    .skills-category:nth-child(1) { animation-delay: 0.1s; }
    .skills-category:nth-child(2) { animation-delay: 0.2s; }
    .skills-category:nth-child(3) { animation-delay: 0.3s; }
    .skills-category:nth-child(4) { animation-delay: 0.4s; }
    .skills-category:nth-child(5) { animation-delay: 0.5s; }
    .skills-category:nth-child(6) { animation-delay: 0.6s; }
    .skills-category:nth-child(7) { animation-delay: 0.7s; }
    .skills-category:nth-child(8) { animation-delay: 0.8s; }
    .skills-category:nth-child(9) { animation-delay: 0.9s; }
    .skills-category:nth-child(10) { animation-delay: 1.0s; }
    .skills-category:nth-child(11) { animation-delay: 1.1s; }
    .skills-category:nth-child(12) { animation-delay: 1.2s; }
    
    .skills-category:hover {
        background: linear-gradient(135deg, rgba(46, 134, 171, 0.18) 0%, rgba(162, 59, 114, 0.12) 50%, rgba(241, 143, 1, 0.1) 100%);
        border-left-color: #F18F01;
        border-color: rgba(241, 143, 1, 0.6);
        box-shadow: 0 8px 25px rgba(46, 134, 171, 0.4);
        transform: translateX(5px) translateY(-2px);
    }
    
    @keyframes slideInLeft {
        from {
            opacity: 0;
            transform: translateX(-30px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .skills-category-title {
        font-size: 1.2em;
        font-weight: 700;
        color: #F18F01;
        margin-bottom: 15px;
        display: block;
        letter-spacing: 0.8px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    
    /* Skills styling */
    .skill-badge {
        display: inline-block;
        background: linear-gradient(135deg, rgba(46, 134, 171, 0.25) 0%, rgba(46, 134, 171, 0.35) 100%);
        color: #e4e4e4;
        padding: 6px 14px;
        margin: 5px 5px 5px 0;
        border-radius: 18px;
        font-size: 0.88em;
        font-weight: 500;
        border: 1px solid rgba(46, 134, 171, 0.6);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .skill-badge::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .skill-badge:hover::before {
        left: 100%;
    }
    
    .skill-badge:hover {
        background: linear-gradient(135deg, rgba(241, 143, 1, 0.35) 0%, rgba(241, 143, 1, 0.45) 100%);
        border-color: #F18F01;
        transform: translateY(-3px) scale(1.05);
        box-shadow: 0 5px 12px rgba(241, 143, 1, 0.4);
        color: #FFF;
    }
    
    /* Certification card styling */
    .cert-card {
        background: rgba(255, 255, 255, 0.05);
        border-left: 4px solid #2E86AB;
        border-radius: 10px;
        padding: 15px 20px;
        margin: 10px 0;
        transition: all 0.3s ease;
    }
    
    .cert-card:hover {
        background: rgba(255, 255, 255, 0.08);
        border-left-color: #F18F01;
        transform: translateX(5px);
        box-shadow: 0 4px 15px rgba(46, 134, 171, 0.2);
    }
    
    .cert-title {
        font-size: 1.1em;
        font-weight: 600;
        color: #F18F01;
        margin-bottom: 8px;
    }
    
    .cert-details {
        font-size: 0.95em;
        color: #a0a0a0;
    }
    
    /* Education card styling */
    .education-card {
        background: linear-gradient(135deg, rgba(46, 134, 171, 0.1) 0%, rgba(162, 59, 114, 0.08) 100%);
        border-radius: 15px;
        padding: 30px;
        margin: 20px 0;
        border: 2px solid rgba(46, 134, 171, 0.3);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .education-card::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(241, 143, 1, 0.1) 0%, transparent 70%);
        transition: all 0.6s ease;
        opacity: 0;
    }
    
    .education-card:hover::before {
        opacity: 1;
        top: -25%;
        right: -25%;
    }
    
    .education-card:hover {
        border-color: rgba(241, 143, 1, 0.5);
        box-shadow: 0 8px 25px rgba(46, 134, 171, 0.3);
        transform: translateY(-5px);
    }
    
    .education-degree {
        font-size: 1.5em;
        font-weight: 700;
        background: linear-gradient(135deg, #2E86AB 0%, #F18F01 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    
    .education-field {
        font-size: 1.2em;
        color: #A23B72;
        font-weight: 600;
        margin-bottom: 15px;
    }
    
    .education-details {
        font-size: 1.05em;
        color: #e4e4e4;
        line-height: 1.8;
    }
    
    .education-details strong {
        color: #F18F01;
    }
    
    /* Contact section fancy styling */
    .contact-hero {
        background: linear-gradient(135deg, rgba(46, 134, 171, 0.15) 0%, rgba(162, 59, 114, 0.12) 50%, rgba(241, 143, 1, 0.1) 100%);
        border-radius: 20px;
        padding: 35px 30px;
        margin: 30px 0;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
        animation: fadeInUp 1s ease-out;
        border: 2px solid rgba(46, 134, 171, 0.3);
        text-align: center;
    }
    
    .contact-hero::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(241, 143, 1, 0.1) 0%, transparent 70%);
        animation: rotate 20s linear infinite;
    }
    
    .contact-hero::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent 30%, rgba(46, 134, 171, 0.05) 50%, transparent 70%);
        animation: shimmer 3s ease-in-out infinite;
    }
    
    .contact-hero > * {
        position: relative;
        z-index: 1;
    }
    
    .contact-hero:hover {
        border-color: rgba(241, 143, 1, 0.5);
        box-shadow: 0 12px 40px rgba(46, 134, 171, 0.4);
        transform: translateY(-3px);
    }
    
    .contact-title {
        font-size: 2em;
        font-weight: 800;
        background: linear-gradient(135deg, #2E86AB 0%, #A23B72 50%, #F18F01 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
        animation: fadeInDown 1s ease-out 0.2s both;
    }
    
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin-top: 20px;
    }
    
    .contact-card {
        background: linear-gradient(135deg, rgba(46, 134, 171, 0.2) 0%, rgba(162, 59, 114, 0.15) 100%);
        border-radius: 12px;
        padding: 20px 18px;
        border: 2px solid rgba(46, 134, 171, 0.3);
        transition: all 0.4s ease;
        animation: fadeInUp 1s ease-out 0.4s both;
        position: relative;
        overflow: hidden;
    }
    
    .contact-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        transition: left 0.5s;
    }
    
    .contact-card:hover::before {
        left: 100%;
    }
    
    .contact-card:hover {
        background: linear-gradient(135deg, rgba(241, 143, 1, 0.25) 0%, rgba(162, 59, 114, 0.2) 100%);
        border-color: #F18F01;
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 8px 25px rgba(241, 143, 1, 0.4);
    }
    
    .contact-icon {
        font-size: 2.2em;
        margin-bottom: 10px;
        display: block;
        animation: pulse 2s ease-in-out infinite;
    }
    
    .contact-label {
        font-size: 0.95em;
        font-weight: 600;
        color: #F18F01;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .contact-value {
        font-size: 1em;
        color: #e4e4e4;
        font-weight: 500;
    }
    
    .contact-value a {
        color: #2E86AB;
        text-decoration: none;
        transition: all 0.3s ease;
        border-bottom: 2px solid transparent;
    }
    
    .contact-value a:hover {
        color: #F18F01;
        border-bottom-color: #F18F01;
    }
    
    /* Section spacing */
    .section-spacer {
        margin-top: 60px;
        margin-bottom: 30px;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2em;
        }
        .hero-subtitle {
            font-size: 1.2em;
        }
        .nav-links {
            gap: 5px;
        }
        .nav-link {
            padding: 8px 15px;
            font-size: 0.85em;
        }
    }
    
    /* Streamlit specific overrides */
    .stMarkdown {
        color: #e4e4e4;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #2E86AB !important;
    }
    
    .stExpander {
        background: linear-gradient(135deg, rgba(46, 134, 171, 0.08) 0%, rgba(162, 59, 114, 0.05) 100%);
        border-radius: 15px;
        border: 2px solid transparent;
        background-clip: padding-box;
        animation: slideInLeft 0.8s ease-out both;
        transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
        margin-bottom: 20px !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    /* Animated gradient border */
    .stExpander::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        border-radius: 15px;
        padding: 2px;
        background: linear-gradient(135deg, #2E86AB, #A23B72, #F18F01);
        background-size: 200% 200%;
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        animation: gradientFlow 4s ease infinite;
        opacity: 0.6;
        z-index: -1;
    }
    
    .stExpander:nth-child(1) {
        animation-delay: 0.1s;
    }
    
    .stExpander:nth-child(2) {
        animation-delay: 0.25s;
    }
    
    .stExpander:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    .stExpander:nth-child(4) {
        animation-delay: 0.55s;
    }
    
    .stExpander:nth-child(5) {
        animation-delay: 0.7s;
    }
    
    /* Shimmer effect */
    .stExpander::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg,
            transparent,
            rgba(255, 255, 255, 0.15),
            transparent);
        transition: left 0.7s ease;
        z-index: 1;
        pointer-events: none;
    }
    
    .stExpander:hover::before {
        left: 100%;
    }
    
    .stExpander:hover {
        background: linear-gradient(135deg, rgba(46, 134, 171, 0.2) 0%, rgba(162, 59, 114, 0.15) 50%, rgba(241, 143, 1, 0.1) 100%);
        transform: translateX(15px) scale(1.02);
        box-shadow: 0 8px 30px rgba(46, 134, 171, 0.4), 0 0 40px rgba(241, 143, 1, 0.2);
    }
    
    .stExpander:hover::after {
        opacity: 1;
        animation-duration: 2s;
    }
    
    /* Experience section wrapper */
    .experience-wrapper {
        animation: fadeInUp 0.8s ease-out both;
        padding: 20px;
        background: linear-gradient(135deg, rgba(46, 134, 171, 0.03) 0%, rgba(162, 59, 114, 0.02) 100%);
        border-radius: 20px;
        margin-top: 20px;
    }
    
    /* Experience header animation */
    #experience + div h2 {
        animation: fadeInDown 0.6s ease-out both;
        background: linear-gradient(135deg, #2E86AB 0%, #A23B72 50%, #F18F01 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-size: 200% 200%;
        animation: fadeInDown 0.6s ease-out both, gradientFlow 5s ease infinite;
        font-size: 2.2em !important;
        font-weight: 700 !important;
        margin-bottom: 30px !important;
        text-align: center;
        position: relative;
        padding-bottom: 15px;
    }
    
    /* Decorative underline for experience header */
    #experience + div h2::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 4px;
        background: linear-gradient(90deg, #2E86AB, #A23B72, #F18F01);
        border-radius: 2px;
        animation: breathe 2s ease-in-out infinite;
    }
    
    /* Expander summary styling */
    .stExpander summary {
        font-weight: 700 !important;
        font-size: 1.15em !important;
        color: #F18F01 !important;
        padding: 15px 20px !important;
        transition: all 0.3s ease;
    }
    
    .stExpander summary:hover {
        color: #2E86AB !important;
        padding-left: 25px !important;
    }
    
    /* Expander content styling */
    .stExpander > div > div {
        padding: 20px 25px !important;
        background: rgba(0, 0, 0, 0.1);
        border-radius: 0 0 15px 15px;
    }
    
    /* Company emoji styling */
    .stExpander summary::before {
        filter: drop-shadow(0 0 8px rgba(241, 143, 1, 0.5));
        animation: pulse 2s ease-in-out infinite;
    }
    
    /* Smooth scroll */
    html {
        scroll-behavior: smooth;
    }
</style>
""", unsafe_allow_html=True)

# Navigation Bar
import base64
import os

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
            <p style="font-size: 1em; color: #F18F01; font-weight: 600; margin: 0;">✅ Eligible to work in the UK · No sponsorship required</p>
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
            <p style="font-size: 1em; color: #F18F01; font-weight: 600; margin: 0;">✅ Eligible to work in the UK · No sponsorship required</p>
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
