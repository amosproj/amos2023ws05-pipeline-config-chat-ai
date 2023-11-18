# app.py
from flask import Flask, request, jsonify
from inference import generate  # Import  generate function
from downloadmodel import download_mpt_quant  # Import the download function


app = Flask(__name__)

# Specify the folder we want to save the downloaded model
destination_folder = "models"

# Download the mpt-7b-chat model when the Flask app starts
repo_id = "mosaicml/mpt-7b-chat"
model_filename = "mpt-7b-chat.ggmlv0.q4_1.bin"
model_path = download_mpt_quant(destination_folder, repo_id, model_filename)


# Use the model path in the generate function
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_prompt = data.get('user_prompt')

    # Call the  generate function with the model_path
    assistant_response = generate(user_prompt, model_path)

    return jsonify({'assistant_response': assistant_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

