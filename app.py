import streamlit as st
import simplifier

# Page Configuration
st.set_page_config(
    page_title="AI Text Simplifier",
    page_icon="✨",
    layout="wide"  # Changed to wide layout for better side-by-side view
)

# Title and Description
st.title("✨ AI Text Simplifier")
st.markdown("Transform complex text into simple, easy-to-understand language using AI.")
st.markdown("---")

# Session State Initialization
if 'input_text' not in st.session_state:
    st.session_state.input_text = ""
if 'simplified_text' not in st.session_state:
    st.session_state.simplified_text = ""

# Complex Examples
examples = {
    "Medical Report (Complex)": """The patient is currently experiencing an acute exacerbation of chronic obstructive pulmonary disease, characterized by significant dyspnea, increased sputum production, and coughing. Auscultation reveals diffuse wheezing and crackles bilaterally. Immediate pharmacological intervention with bronchodilators and corticosteroids is indicated to alleviate airway obstruction and reduce inflammation.""",
    
    "Legal Contract (Complex)": """Notwithstanding anything to the contrary contained herein, the party of the first part shall not be liable for any consequential, incidental, or indirect damages arising out of the performance or non-performance of this agreement, even if advised of the possibility of such damages, except in cases of gross negligence or willful misconduct.""",

    "Academic/Linguistic (Complex)": """The utilization of utilizing a complex vocabulary is often considered an indication of intelligence, however, in many instances, it merely serves to obfuscate the intended meaning and alienate the audience. Effective communication necessitates clarity and conciseness rather than verbosity."""
}

# Callback to load example
def load_example():
    st.session_state.input_text = examples[st.session_state.selected_example]

# Layout: Side-by-Side
col1, col2 = st.columns(2, gap="medium")

with col1:
    st.subheader("Input Text")
    
    # Example Selector
    st.selectbox(
        "Choose an example to load:", 
        options=list(examples.keys()), 
        key="selected_example",
        on_change=load_example
    )
    
    # Input Area
    input_text = st.text_area(
        "Enter your complex text here:", 
        height=300, 
        key="input_text"
    )
    
    # Simplify Button
    if st.button("Simplify Text", type="primary", use_container_width=True):
        if not input_text or not input_text.strip():
            st.warning("Please enter some text to simplify.")
        elif len(input_text) > 1000:
            st.error(f"Input text exceeds 1000 characters ({len(input_text)}/1000). Please shorten it.")
        else:
            with st.spinner("Simplifying..."):
                try:
                    # Call backend
                    result = simplifier.simplify_text(input_text)
                    st.session_state.simplified_text = result
                except Exception as e:
                    st.error(f"An error occurred: {e}")

with col2:
    st.subheader("Simplified Output")
    # Output Area (Read-only/Display)
    if st.session_state.simplified_text:
        st.success("Simplification Complete!")
        st.info(st.session_state.simplified_text)
    else:
        st.text_area(
            "Output will appear here:",
            value="",
            height=300,
            disabled=True,
            placeholder="Simplified text will be shown here..."
        )

# Footer
st.markdown("---")
st.caption("Powered by HuggingFace Transformers (google/flan-t5-small)")
