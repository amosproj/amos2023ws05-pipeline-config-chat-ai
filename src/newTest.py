import os
import re
import itertools

def extract_names(folder_path):
    names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    matches = re.findall(r'class (\w+)\(', content)
                    if matches:
                        names.append(matches[0])
    return names

rag_folder = "C:\\Users\\lynda\\OneDrive\\Bureau\\pc\\amos2023ws05-pipeline-config-chat-ai\\src\\RAG"
pipelines_folder = os.path.join(rag_folder, "pipelines")

sources_folder = os.path.join(pipelines_folder, "sources")
transformers_folder = os.path.join(pipelines_folder, "transformers")
destinations_folder = os.path.join(pipelines_folder, "destinations")

source_names = extract_names(sources_folder)
transformer_names = extract_names(transformers_folder)
destination_names = extract_names(destinations_folder)

combinations = list(itertools.product(source_names, transformer_names, destination_names))

query_template = "I would like to use RTDIP components to read from an eventhub using 'connection string' as the connection string, and 'consumer group' as the consumer group, transform using {transformer} and {edge_transformer} then write to {destination}"

for combo in combinations:
    query = query_template.format(transformer=combo[1], edge_transformer=combo[1] + "Edge", destination=combo[2])
    print(query)
