import streamlit as st
from scrape import (
    scrape_website,
    extract_body_content,
    clean_body_content,
    split_dom_content,
)

# Streamlit UI
st.title("Web Scraper")
st.markdown("---")

url = st.text_input("Enter Website URL")

# Step 1: Scrape the Websitea
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

# Step 2: Display Content Analysis
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

# Information about AI features
st.markdown("---")
st.info("""
**Note:** AI parsing features are currently disabled for deployment compatibility. 
This version provides web scraping and content analysis without AI processing.
To enable AI features, you would need to:
1. Use external AI APIs (OpenAI, Anthropic, etc.)
2. Deploy Ollama separately
3. Use Render's built-in AI services
""")
