from pyspark.sql import SparkSession
from pyspark.sql.functions import size, split
import transformers

# Initialize Spark Session
spark = SparkSession.builder.appName('ChatWithPySpark').getOrCreate()

# Load the MPT30B model
model = transformers.AutoModelForCausalLM.from_pretrained(
    'mosaicml/mpt-7b-chat',
    trust_remote_code=True
)
tokenizer = transformers.AutoTokenizer.from_pretrained('mosaicml/mpt-7b-chat')

def generate_response(user_message):
    """
    Generate a response using the MPT30B model for a given user message.
    """
    # Tokenize and generate response
    inputs = tokenizer.encode(user_message, return_tensors='pt')
    reply_ids = model.generate(inputs, max_length=1024)
    bot_reply = tokenizer.decode(reply_ids[0], skip_special_tokens=True)
    return bot_reply

user_message = "What do you know about RTDIP-SDK pipeline configurations?"
response = generate_response(user_message)
print(f"Bot: {response}")
