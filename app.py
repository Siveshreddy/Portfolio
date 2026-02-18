import streamlit as st

# Page Configuration
st.set_page_config(page_title="Sudharsan B | Portfolio", page_icon="💻", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.title("Contact Info")
    st.write("📍 Chengalpattu, 603002")
    st.write("📧 sudarshanabs2223@gmail.com")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/sudharsancse)")
    st.write("📞 +91 9943995954")
    
    st.divider()
    st.subheader("Languages")
    st.write("Tamil, English, Telugu")

# --- HEADER SECTION ---
st.title("SUDHARSAN B")
st.subheader("Software Trainee | Java & Python Developer")
st.write(
    "Dedicated Software Trainee with a commitment to excellence and a strong technical skill set in Java and Python. "
    "Focused on continuous growth and adaptability. Thrives in collaborative environments and seeks to create impactful "
    "solutions while achieving set objectives."
)

# --- SKILLS SECTION ---
st.divider()
st.header("Technical Skills")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 💻 Languages")
    st.write("- Java")
    st.write("- Python")
    st.write("- SQL")
with col2:
    st.markdown("### 🌐 Web & Tools")
    st.write("- HTML5, CSS")
    st.write("- Flask, Streamlit")
    st.write("- Canva, Photoshop, Excel")
with col3:
    st.markdown("### 🛠️ Concepts")
    st.write("- Manual Testing")
    st.write("- UI/UX Concepts")
    st.write("- Digital Marketing")

# --- EXPERIENCE ---
st.divider()
st.header("Experience & Internships")

# Experience 1
st.subheader("Full Stack Java Intern | Vei Technologies")
st.caption("Chennai, India | Internship")
st.write(
    """
    - Gained comprehensive hands-on experience in Java programming and full-stack development.
    - Developed and tested software modules, ensuring high performance and responsiveness.
    """
)

# Experience 2
st.subheader("UI/UX Design Intern | Ceeras IT Services")
st.caption("Chennai, India | Internship")
st.write(
    """
    - Applied principles of user interface design to create intuitive and user-friendly web layouts.
    - Collaborated with the design team to optimize user experience flows.
    """
)

# Experience 3
st.subheader("Robotics Trainee | Vei Technologies Pvt Ltd")
st.caption("Chennai, India | Training")
st.write("- Participated in intensive training focused on robotics technology and automation systems.")

# --- PROJECTS ---
st.divider()
st.header("Projects")
st.subheader("Real Time Language Learning Assistance Using AI")
st.write("**Tech Stack:** Python, NLP")
st.write(
    """
    - Developed an AI-driven application using Python and Natural Language Processing (NLP) to facilitate real-time language translation.
    - Implemented speech-to-text and text-to-speech functionalities to improve pronunciation and user interactivity.
    - Designed a user-friendly interface that provides instant feedback to users, aiding in vocabulary retention.
    """
)

# --- EDUCATION ---
st.divider()
st.header("Education")

edu1, edu2 = st.columns(2)
with edu1:
    st.write("**Adhiparasakthi Engineering College**")
    st.write("- B.E. Computer Science (2021-2025)")
    st.write("- Percentage: 85% (No History Of Arrears)")

with edu2:
    st.write("**Narayana e-techno Higher Secondary School**")
    st.write("- Higher Secondary (12th) | Passed: 2021")
    st.write("- Percentage: 70%")

# --- CERTIFICATIONS ---
st.divider()
st.header("Certifications")
cert_col1, cert_col2 = st.columns(2)
with cert_col1:
    st.write("- **Java Full Stack** (QSpiders)")
    st.write("- **Programming in Java** (NPTEL)")
    st.write("- **Python Programming** (CodeChef)")
with cert_col2:
    st.write("- **HTML5** (Infosys)")
    st.write("- **Digital Marketing** (Infosys)")

# --- INTERESTS ---
st.divider()
st.header("Interests")
st.write("Watching Movies, Playing Virtual Games")