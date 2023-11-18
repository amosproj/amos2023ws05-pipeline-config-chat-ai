import os
from huggingface_hub import hf_hub_download

def download_mpt_quant(destination_folder: str, repo_id: str, model_filename: str):
    local_path = os.path.abspath(destination_folder)
    model_path = hf_hub_download(
        repo_id=repo_id,
        
        filename=model_filename,
        local_dir=local_path,
        local_dir_use_symlinks=True
    )
    return model_path


if __name__ == "__main__":
    repo_id = "mosaicml/mpt-7b-chat"
    model_filename = "mpt-7b-chat.ggmlv0.q4_1.bin"
    destination_folder = "models"
    download_mpt_quant(destination_folder, repo_id, model_filename)