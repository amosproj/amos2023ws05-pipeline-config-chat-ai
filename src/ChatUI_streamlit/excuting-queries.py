#%%
from LLMModel import RAG   
import random
import json
#%%
def load_queries(file_path):
    with open(file_path, 'r') as file:
        queries = file.readlines()
    return queries

def select_random_queries(queries, number=10):
    return random.sample(queries, number)

def get_rag_response(query):
    return RAG.run(query.strip())

def save_to_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
#%%
def main():
    file_path = '/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/TESTS/output_queries.txt'
    output_json_path = '/Users/zainhazzouri/projects/amos2023ws05-pipeline-config-chat-ai/src/ChatUI_streamlit/results.json'

    queries = load_queries(file_path)
    random_queries = select_random_queries(queries)

    query_response_objects = []

    for query in random_queries:
        response = get_rag_response(query)
        query_response_objects.append({
            "query": query.strip(),
            "response": response
        })

    save_to_json(query_response_objects, output_json_path)

if __name__ == "__main__":
    main()
# %%
