from flask import Flask, render_template, request, jsonify
from pyspark.sql import SparkSession
from pyspark.sql.functions import size, split

app = Flask(__name__)

# Initialize Spark Session
spark = SparkSession.builder.appName('ChatWithPySpark').getOrCreate()

@app.route('/')
def home():
    return render_template('webpage.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json['message']
    
    # Use PySpark to count the number of words in the user's message
    df = spark.createDataFrame([(user_message,)], ['message'])
    df = df.withColumn('words', split(df['message'], ' '))
    df = df.withColumn('wordCount', size(df['words']))
    word_count = df.first()['wordCount']
    
    # Logging the DataFrame show output (not required for production)
    df.show()

    # Craft a response that includes the word count, the original user message, and indicates the sender
    response_message = {
        "message": f"Bot: Your message has {word_count} words.",
        "userMessage": f"You: {user_message}",
        "sender": "Bot"
    }
    return jsonify(response_message)

if __name__ == "__main__":
    app.run(debug=True)
