import gradio as gr
from transformers import pipeline

# Model path has been changed
# model_path = "./My_Sinhala_Hate_Speech_Model"
model_path = "dimuthulk/sinhala-hate-speech-detector"

print("Model is loading. Please wait...")

# Loading the model
detector = pipeline("text-classification", model=model_path, tokenizer=model_path)

# Function to generate the result
def predict_hate_speech(text):
    if not text.strip():
        return "Please enter a sentence to check."
        
    result = detector(text)[0]
    label = result['label']
    score = round(result['score'] * 100, 2)
    
    if label == 'OFF':
        return f"⚠️ Warning! This appears to be an offensive sentence. (Confidence: {score}%)"
    else:
        return f"✅ This is a normal (Not Offensive) sentence. (Confidence: {score}%)"

# New modern theme and text size
custom_theme = gr.themes.Soft(
    text_size=gr.themes.sizes.text_lg, 
    spacing_size=gr.themes.sizes.spacing_lg,
    radius_size=gr.themes.sizes.radius_md
)

with gr.Blocks() as demo:
    
    # Color removed from title to be compatible with both Dark/Light mode
    gr.Markdown("<h1 style='text-align: center; font-weight: bold;'>🛡️ Sinhala (සිංහල) Hate Speech Detector</h1>")
    gr.Markdown("<p style='text-align: center; font-size: 1.1em;'>This application can detect whether a Sinhala sentence contains offensive content.<br>මෙම යෙදුම මගින් සිංහල වාක්‍යයක අපහාසාත්මක (Offensive) අදහසක් තිබේදැයි හඳුනාගත හැක.</p>")
    
    with gr.Column(elem_classes="container"):
        # 1. Text input area
        input_text = gr.Textbox(
            lines=4, 
            placeholder="Enter the Sinhala sentence you want to check here...", 
            label="📝 Your Sentence"
        )
        
        # 2. Check button
        submit_btn = gr.Button("Check 🔍", variant="primary", size="lg")
        
        # 3. Result display area
        output_text = gr.Textbox(
            label="💡 Result", 
            lines=2,
            interactive=False
        )
    
    # Function to execute when button is clicked
    submit_btn.click(
        fn=predict_hate_speech, 
        inputs=input_text, 
        outputs=output_text
    )

# Run the app
if __name__ == "__main__":
    demo.launch(theme=custom_theme)