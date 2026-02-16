import streamlit as st
import simplifier

# Page Configuration
st.set_page_config(
    page_title="AI Text Simplifier",
    page_icon="✨",
    layout="centered"
)

# Title and Description
st.title("✨ AI Text Simplifier")
st.markdown("Transform complex text into simple, easy-to-understand language using AI.")

# Session State Initialization
if 'input_text' not in st.session_state:
    st.session_state.input_text = ""

# Callback to load example
def load_example():
    st.session_state.input_text = "The utilization of utilizing a complex vocabulary is often considered an indication of intelligence."

# UI Layout
col1, col2 = st.columns([3, 1])
with col2:
    st.button("Load Example", on_click=load_example)

# Input Area (linked to session handling via key)
input_text = st.text_area("Enter your text here:", height=200, key="input_text")

# Simplify Button
if st.button("Simplify Text", type="primary"):
    if not input_text or not input_text.strip():
        st.warning("Please enter some text to simplify.")
    elif len(input_text) > 1000:
        st.error(f"Input text exceeds 1000 characters ({len(input_text)}/1000). Please shorten it.")
    else:
        with st.spinner("Simplifying..."):
            try:
                # Call backend
                result = simplifier.simplify_text(input_text)
                
                # Display Result
                st.success("Simplification Complete!")
                st.markdown("### Simplified Text:")
                st.info(result)
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.caption("Powered by HuggingFace Transformers (google/flan-t5-small)")
