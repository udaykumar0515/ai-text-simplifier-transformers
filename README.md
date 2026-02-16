# AI Text Simplifier

A web application that converts complex text into simple, easy-to-understand language using AI-powered natural language processing.

## Live Demo

[https://ai-text-simplifier.streamlit.app/](https://ai-text-simplifier.streamlit.app/)

## Features

- AI-powered text simplification using HuggingFace Transformers
- Side-by-side comparison interface
- Pre-loaded domain-specific examples (Medical, Legal, Academic)
- Input validation and error handling
- Efficient model caching for faster performance

## Technology Stack

- **Frontend**: Streamlit
- **Backend**: HuggingFace Transformers (PyTorch)
- **Model**: google/flan-t5-small
- **Language**: Python 3.8+

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/udaykumar0515/ai-text-simplifier-transformers.git
   cd ai-text-simplifier-transformers
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application locally:

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## Example

**Input:**
> The patient is currently experiencing an acute exacerbation of chronic obstructive pulmonary disease, characterized by significant dyspnea, increased sputum production, and coughing.

**Output:**
> The patient has a worsening of chronic lung disease with breathing difficulties, increased mucus, and coughing.

## Project Structure

```
.
├── app.py              # Streamlit frontend
├── simplifier.py       # Text simplification backend
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # Documentation
```

## Requirements

- Python 3.8 or higher
- streamlit
- transformers
- torch
- sentencepiece

## License

This project is available for educational and research purposes.
