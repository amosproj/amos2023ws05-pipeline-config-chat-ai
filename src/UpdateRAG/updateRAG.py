import subprocess
import os
import shutil
import tempfile


def run_command(command, work_dir=None):
    process = subprocess.Popen(command, shell=True, text=True, cwd=work_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return stdout.strip(), stderr.strip()

# Tempo directory for sparse checkout
#sparse_checkout_dir = "C:\\Users\\lynda\\OneDrive\\Bureau\\test"
current_script_dir = os.path.dirname(os.path.abspath(__file__))
local_directory = os.path.join(current_script_dir, '..', 'RAG', 'pipelines')
local_directory = os.path.abspath(local_directory)


with tempfile.TemporaryDirectory() as sparse_checkout_dir:
    
    rtdip_repo_url = 'https://github.com/rtdip/core.git'
    specific_directory = 'src/sdk/python/rtdip_sdk/pipelines'

    # Initialiser the local repo for sparse checkout
    run_command(f'git init', sparse_checkout_dir)
    run_command(f'git remote add -f origin {rtdip_repo_url}', sparse_checkout_dir)
    run_command('git config core.sparseCheckout true', sparse_checkout_dir)

    # Write the specific direc we want to checkout to the sparse-checkout file
    with open(os.path.join(sparse_checkout_dir, '.git', 'info', 'sparse-checkout'), 'w') as sparse_checkout_file:
        sparse_checkout_file.write(specific_directory + '/*\n')

    # Pull the direc from the develop branch of rtdip repo
    run_command('git pull origin develop', sparse_checkout_dir)

    # Find the directory path in the sparse checkout that correspond to the 'pipelines' direc
    checkout_pipelines_path = os.path.join(sparse_checkout_dir, specific_directory)

    # Compare and copy the changes to our local directory
    for root, dirs, files in os.walk(checkout_pipelines_path):
        local_root = root.replace(checkout_pipelines_path, local_directory)
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(local_root, file)
            os.makedirs(os.path.dirname(dst_file), exist_ok=True)
            shutil.copy2(src_file, dst_file)
            print(f"Copied '{src_file}' to '{dst_file}'")

    print("Update process completed.")
