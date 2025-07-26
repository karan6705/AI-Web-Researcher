import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)
from parse import parse_with_gemini
from config import AVAILABLE_MODELS, DEFAULT_MODEL, MODEL_DESCRIPTIONS

# Streamlit UI
st.title("AI Web Scraper")
st.markdown("---")

# Model Selection
st.subheader("Choose AI Model")
selected_model = st.selectbox(
    "Select the AI model for parsing:",
    options=list(AVAILABLE_MODELS.keys()),
    index=list(AVAILABLE_MODELS.keys()).index(DEFAULT_MODEL),
    format_func=lambda x: f"{x} - {MODEL_DESCRIPTIONS[x]}"
)

url = st.text_input("Enter Website URL")

# Step 1: Scrape the Website
if st.button("Scrape Website"):
    if url:
        st.write("Scraping the website...")

        try:
            # Scrape the website
            dom_content = scrape_website(url)
            body_content = extract_body_content(dom_content)
            cleaned_content = clean_body_content(body_content)

            # Store the DOM content in Streamlit session state
            st.session_state.dom_content = cleaned_content

            # Display the DOM content in an expandable text box
            with st.expander("View Scraped Content"):
                st.text_area("Scraped Content", cleaned_content, height=300)

            st.success("Website scraped successfully!")

        except Exception as e:
            st.error(f"Error scraping website: {str(e)}")

# Step 2: AI Content Parsing
if "dom_content" in st.session_state:
    st.subheader("AI Content Parsing")

    parse_description = st.text_area(
        "Describe what you want to parse from the content")

    if st.button("Parse Content with AI"):
        if parse_description:
            st.write(f"Parsing the content using {selected_model}...")

            # Parse the content with Gemini using selected model
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_gemini(
                dom_chunks, parse_description, AVAILABLE_MODELS[selected_model])

            st.subheader("AI Parsing Results")
            st.write(parsed_result)

# Step 3: Content Analysis
if "dom_content" in st.session_state:
    st.subheader("Content Analysis")

    # Split content into chunks for analysis
    dom_chunks = split_dom_content(st.session_state.dom_content)

    # Display basic statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Characters", len(st.session_state.dom_content))
    with col2:
        st.metric("Number of Chunks", len(dom_chunks))
    with col3:
        st.metric("Average Chunk Size", len(
            st.session_state.dom_content) // len(dom_chunks) if dom_chunks else 0)

    # Display chunks
    with st.expander("View Content Chunks"):
        for i, chunk in enumerate(dom_chunks, 1):
            st.write(f"**Chunk {i}:**")
            st.text_area(f"Chunk {i} Content", chunk,
                         height=150, key=f"chunk_{i}")
            st.markdown("---")

# Information about the app
st.markdown("---")
st.info("""
**AI Web Scraper powered by Google Gemini API**

This application now uses Google's Gemini API for AI-powered content parsing.
Make sure your GEMINI_API_KEY environment variable is set in Render.
""")
