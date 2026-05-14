# Aettalli Sai Prabha - Portfolio Website

A modern, interactive portfolio website built with Python and Streamlit showcasing professional experience, skills, and achievements in AI Engineering, Automation, and Data Engineering.

## Features

- 🎨 Modern, responsive design with custom CSS styling
- 🤖 Comprehensive showcase of AI/ML and automation projects
- 📊 Interactive sections for experience, skills, and achievements
- 🎯 Clean, professional layout inspired by modern portfolio designs
- 🐍 100% Python - no JavaScript required!

## Technologies Used

- **Python 3.8+**
- **Streamlit** - Web application framework
- **Custom CSS** - For styling and animations

## Installation

1. Clone this repository or download the files:
```bash
git clone <your-repo-url>
cd Portfolio
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Running the Portfolio

1. Make sure you're in the project directory and your virtual environment is activated

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. The portfolio will open automatically in your default browser at `http://localhost:8501`

## Project Structure

```
Portfolio/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Sections

The portfolio includes the following sections:

1. **Hero Section** - Introduction and title
2. **Professional Profile** - Career summary and expertise
3. **Key Achievements** - Quantifiable results and impact
4. **Professional Experience** - Detailed work history with 5 companies
5. **Core Skills** - Technical skills organized by category
6. **Certifications** - Professional certifications and training
7. **Education** - Academic background
8. **Contact** - Contact information and availability

## Customization

To customize the portfolio for your own use:

1. **Update Personal Information**: Edit the content in `app.py` functions like `render_hero()`, `render_profile()`, etc.

2. **Change Colors**: Modify the CSS variables in the `st.markdown()` section at the top of `app.py`:
   - `--primary-color`: Main theme color
   - `--secondary-color`: Secondary accent color
   - `--accent-color`: Highlight color

3. **Add/Remove Sections**: Add new functions following the pattern of existing `render_*()` functions

## Deployment Options

### Streamlit Cloud (Free)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy!

### Heroku
1. Create a `Procfile`:
```
web: sh setup.sh && streamlit run app.py
```

2. Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

3. Deploy to Heroku

### Local Network Access
To make the portfolio accessible on your local network:
```bash
streamlit run app.py --server.address 0.0.0.0
```

## Browser Compatibility

The portfolio is tested and works on:
- ✅ Chrome/Edge (Chromium)
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers

## Performance

- Fast loading times
- Responsive design for all screen sizes
- Optimized CSS animations
- No external dependencies beyond Streamlit

## License

This portfolio template is free to use and modify for personal or commercial purposes.

## Contact

**Aettalli Sai Prabha**
- 📧 Email: saiprabha2904@gmail.com
- 📱 Phone: +44 7442 773597
- 💼 LinkedIn: [linkedin.com/in/saiprabha29](https://linkedin.com/in/saiprabha29)
- 🇬🇧 Location: United Kingdom

---

Built with ❤️ using Python & Streamlit