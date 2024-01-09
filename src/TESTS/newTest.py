import os
import re
import itertools

def extract_names(folder_path, exclude_names=None):
    if exclude_names is None:
        exclude_names = []
    names = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Exclude files with ‘interface’ in the name and ‘_init_.py’
            if (file.endswith(".py") and "interface" not in file 
                and file not in exclude_names and file != "__init__.py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()
                    matches = re.findall(r"class (\w+)\(", content)
                    for match in matches:  # Changed to loop over all matches
                        names.append(match)
    return names

rag_folder = "C:\\Users\\lynda\\OneDrive\\Bureau\\pc\\amos2023ws05-pipeline-config-chat-ai\\src\\RAG"
pipelines_folder = os.path.join(rag_folder, "pipelines")

sources_folder = os.path.join(pipelines_folder, "sources")
transformers_folder = os.path.join(pipelines_folder, "transformers")
destinations_folder = os.path.join(pipelines_folder, "destinations")

# Exclude specific names from the lists
exclude_names = ['SourceInterface', 'DestinationInterface', 'TransformerInterface']
source_names = extract_names(sources_folder, exclude_names)
transformer_names = extract_names(transformers_folder, exclude_names)
destination_names = extract_names(destinations_folder, exclude_names)

def filter_components(source_list, destination_list):
    # Filter out elements that do not end with the specified suffix
    source_list = [source for source in source_list if source.endswith("Source")]
    destination_list = [destination for destination in destination_list if destination.endswith("Destination")]
    return source_list, destination_list

filtered_sources, filtered_destinations = filter_components(source_names, destination_names)

num_sources = len(filtered_sources)
num_transformers = len(transformer_names)
num_destinations = len(filtered_destinations)

combinations = list(itertools.product(filtered_sources, transformer_names, filtered_destinations))

query_template = "I would like to use RTDIP components to read from {source}, transform using {transformer}, then write to {destination}"

output_file_path = "output_queries.txt"
num_queries = 0

with open(output_file_path, "w") as output_file:
    for combo in combinations:
        query = query_template.format(source=combo[0], transformer=combo[1], destination=combo[2])
        output_file.write(f"Query {num_queries + 1}: {query}\n")
        num_queries += 1

print(f"Queries have been written to {output_file_path}")
print(f"Total number of queries: {num_queries}")
print(f"Number of sources: {num_sources}")
print(f"Number of transformers: {num_transformers}")
print(f"Number of destinations: {num_destinations}")



