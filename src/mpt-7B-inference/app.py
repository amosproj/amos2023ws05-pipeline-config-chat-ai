# app.py
from flask import Flask, request, jsonify
from inference import generate, load_model_and_tokenizer ,format_prompt  

app = Flask(__name__)

# Load the mpt-7b-chat model and tokenizer from the Hugging Face Model Hub
model_name = "mosaicml/mpt-7b-chat"
llm, tokenizer = load_model_and_tokenizer(model_name, trust_remote_code=True)  # Update model loading

# Use the model and tokenizer in the generate function
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_prompt = data.get('user_prompt')

    # Update the call to use the loaded model and tokenizer directly
    generation_config = {
        "temperature": 0.2,
        "top_k": 0,
        "top_p": 0.9,
        "repetition_penalty": 1.0,
        "max_new_tokens": 512,
    }
    
    # Format the prompt using the system prompt
    system_prompt = "A conversation between a user and an LLM-based AI assistant named Local Assistant. Local Assistant gives helpful and honest answers."
    prompt = format_prompt(system_prompt, user_prompt)
    
    # Generate the assistant's response
    assistant_response = generate(llm, tokenizer, generation_config, prompt)

    return jsonify({'assistant_response': assistant_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
