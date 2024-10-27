import json
import warnings

MODEL_DIRECTORY = "/dlabscratch1/public/llm_weights/model_directory.json"

def model_path(model_name: str) -> str:
    try:
        with open(MODEL_DIRECTORY, "r") as f:
            model_directory = json.load(f)
    except FileNotFoundError:
        warnings.warn(f"Model directory {MODEL_DIRECTORY} not found.")
        return model_name

    if model_name not in model_directory:
        warnings.warn(f"Model {model_name} not found in DLAB LLM weights directory, defaulting to huggingface.")
        return model_name
    return model_directory[model_name]

def available_models() -> list[str]:
    try:
        with open(MODEL_DIRECTORY, "r") as f:
            model_directory = json.load(f)
    except FileNotFoundError:
        warnings.warn(f"Model directory {MODEL_DIRECTORY} not found.")
        return []
    return list(model_directory.keys())
