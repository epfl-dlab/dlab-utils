from huggingface_hub import snapshot_download
import json
import warnings
import os
import json
import datetime

MODEL_HUB = "/dlabscratch1/public/llm_weights/"
# V2 will be the new model directory format. Will be removed in the future and only V2 will be supported.
MODEL_DIRECTORY_V2 = MODEL_HUB + "model_directory_v2.json"
MODEL_DIRECTORY_V1 = MODEL_HUB + "model_directory.json"
cwd = os.getcwd()

def download_model(repo_id: str):
    print(f"DLABUTILS: Downloading model {repo_id} to {MODEL_HUB}")
    # to target directory
    snapshot_download(
        repo_id=repo_id,
        local_dir_use_symlinks=False,
        local_dir=os.path.join(MODEL_HUB, repo_id.split("/")[-1]),
        ignore_patterns=["original/**"],
    )

    # reload model directory to ensure non-blocking
    model_directory = get_model_directory()

    # save to model_directory.json
    model_directory[repo_id] = {
        "path": os.path.join(MODEL_HUB, repo_id.split("/")[-1]),
        "download_date": datetime.datetime.now().isoformat(),
        "user": os.environ.get("USER", "unknown"),
    }

    with open(MODEL_DIRECTORY_V2, "w") as f:
        json.dump(model_directory, f)

def get_model_directory() -> dict:
    # Will be removed in the future
    try:
        with open(MODEL_DIRECTORY_V2, "r") as f:
            model_directory = json.load(f)
    except FileNotFoundError:
        with open(MODEL_DIRECTORY_V1, "r") as f:
            model_directory = json.load(f)
    return model_directory

def model_path(model_name: str) -> str:
    try:
        model_directory = get_model_directory()
    except FileNotFoundError:
        warnings.warn(f"DLABUTILS: Model directory {MODEL_DIRECTORY_V1} not found.")
        return model_name

    if model_name not in model_directory:
        warnings.warn(f"DLABUTILS: Model {model_name} not found in DLAB LLM weights directory. Adding to directory...")
        download_model(model_directory, model_name)
    return model_directory[model_name]["path"]

def available_models() -> list[str]:
    try:
        model_directory = get_model_directory()
    except FileNotFoundError:
        warnings.warn(f"DLABUTILS: Model directory {MODEL_DIRECTORY_V1} not found.")
        return []
    return list(model_directory.keys())
