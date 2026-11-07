import streamlit as st

# ---------------------------------------------------------
# THE DAILY JOURNAL - Single-file blog website
# Run with: streamlit run app.py
# ---------------------------------------------------------

st.set_page_config(
    page_title="The Daily Journal",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
.stApp {
    background: #faf9f6;
    color: #242424;
}
.block-container {
    max-width: 1180px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}
h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #242424;
}
.brand {
    font-family: 'Playfair Display', serif;
    font-size: 1.75rem;
    font-weight: 700;
    color: #242424;
}
.brand span, .accent {
    color: #b17c50;
}
.eyebrow {
    color: #a87953;
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: 2px;
}
.hero {
    background: #f0ebe4;
    border-radius: 12px;
    padding: 3.2rem;
    margin: 1.5rem 0 2.5rem 0;
}
.hero h1 {
    font-size: clamp(2.8rem, 6vw, 4.7rem);
    line-height: 1.08;
    margin: .5rem 0 1rem 0;
}
.hero p {
    color: #68645f;
    max-width: 580px;
    font-size: 1.03rem;
}
div[data-testid="stImage"] img {
    border-radius: 9px;
}
.blog-card {
    background: #ffffff;
    border: 1px solid #eee9e3;
    border-radius: 10px;
    padding: 1rem;
    min-height: 285px;
    margin-bottom: .7rem;
}
.blog-card h3 {
    font-size: 1.25rem;
    margin: .45rem 0;
}
.blog-card p {
    color: #77716b;
    font-size: .9rem;
}
.category-label {
    color: #a87953;
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.meta {
    color: #99918a;
    font-size: .78rem;
}
