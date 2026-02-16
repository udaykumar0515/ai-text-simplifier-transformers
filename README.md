# AI Text Simplifier

An AI-powered web application that transforms complex text into simple, easy-to-understand language using HuggingFace Transformers.

## 🚀 Features

- **AI-Powered Simplification**: Uses `google/flan-t5-small` for accurate text simplification.
- **Clean Interface**: Minimalist and responsive UI built with Streamlit.
- **Fast & Efficient**: Optimized model loading with caching and warm-up strategies.
- **Input Validation**: Ensures text is within processing limits for stability.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: HuggingFace Transformers (PyTorch)
- **Model**: `google/flan-t5-small`
- **Language**: Python 3.8+

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone REPO_LINK_PLACEHOLDER
   cd ai-text-simplifier-transformers
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ How to Run

Run the application locally:

```bash
streamlit run app.py
```

## 📝 Example

**Input:**
> "The utilization of utilizing a complex vocabulary is often considered an indication of intelligence."

**Output:**
> "A complex vocabulary is often considered an indication of intelligence."

## 🔮 Future Scope

- Support for multiple languages.
- Adjustable simplification levels (e.g., child, teen, adult).
- File upload support (PDF/Docx).
- API endpoint for external integration.

---
Built with ❤️ using Transformers & Streamlit.
