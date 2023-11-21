# app.py
from flask import Flask, request, jsonify
from inference import generate, load_model_from_hub



app = Flask(__name__)

# Specify the folder we want to save the downloaded model
destination_folder = "models"

# Load the mpt-7b-chat model from the Hugging Face Model Hub
model_name = "mosaicml/mpt-7b-chat"
llm = load_model_from_hub(model_name)


# Use the model path in the generate function
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_prompt = data.get('user_prompt')

# Update the call to use the loaded model directly
    assistant_response = generate(llm, user_prompt)

    return jsonify({'assistant_response': assistant_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


