import functools
import time
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Global/Singleton-like pattern using lru_cache for model loading
@functools.lru_cache(maxsize=1)
def load_model():
    """
    Loads the T5 model and tokenizer.
    Cached to ensure it's loaded only once.
    """
    print("Loading model...")
    model_name = "google/flan-t5-small"
    try:
        tokenizer = T5Tokenizer.from_pretrained(model_name, legacy=False)
        model = T5ForConditionalGeneration.from_pretrained(model_name)
        
        # Warm-up step
        print("Warming up model...")
        dummy_input = "simplify: this is a test"
        inputs = tokenizer(dummy_input, return_tensors="pt", max_length=512, truncation=True)
        model.generate(
            **inputs, 
            max_new_tokens=10,
            num_beams=1,
            early_stopping=True
        )
        print("Model loaded and warmed up.")
        return tokenizer, model
    except Exception as e:
        print(f"Error loading model: {e}")
        raise e

def simplify_text(text: str) -> str:
    """
    Simplifies the input text using the loaded T5 model.
    """
    if not text or not text.strip():
        return ""

    # Input validation (sanity check, though frontend should handle this too)
    if len(text) > 1000:
        # In a real app we might raise an error, but here we'll truncate or warn
        # For now, let's just proceed but maybe the frontend handles the block
        # The user requirement said: "if text length > 1000 ... do NOT run model"
        # So we should probably check and return a message or empty if called directly?
        # But this function is "simplify_text", so maybe raise ValueError?
        # Let's assume frontend checks, but for safety:
        raise ValueError("Input text exceeds 1000 characters.")

    # try-except block removed to allow proper error handling by caller
    tokenizer, model = load_model()
    
    # Improved prompt as per audit feedback
    input_text = "Rewrite the following text in simple English: " + text
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    
    # Generation parameters as requested
    outputs = model.generate(
        **inputs, 
        max_new_tokens=128,
        num_beams=4,
        early_stopping=True
    )
    
    simplified_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return simplified_text

if __name__ == "__main__":
    # Temporary test block (Step 3)
    print("Running local test...")
    complex_text = "The utilization of utilizing a complex vocabulary is often considered an indication of intelligence."
    try:
        result = simplify_text(complex_text)
        print(f"Original: {complex_text}")
        print(f"Simplified: {result}")
        
        # Test warm-up and cache by calling again
        print("Testing cache...")
        start = time.time()
        simplify_text("Another test.")
        print(f"Second call took: {time.time() - start:.4f}s")
        
    except Exception as e:
        print(f"Test failed: {e}")
