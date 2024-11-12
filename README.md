# DLAB utils
Python Library for DLAB utils

## Installation

You can install the `dlabutils` package using pip:

```bash
pip install git+https://github.com/epfl-dlab/dlab-utils.git
```

## Usage

### Model Paths

The `model_path` function returns the path to the model weights given the huggingface identifier, if the model is available in the DLAB LLM weights directory, and defaults to the hf model name if it is not. The `available_models` function returns a list of all available models. Here's a quick tutorial:

```python
from dlabutils.paths import model_path, available_models
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(model_path("meta-llama/Meta-Llama-3-8B-Instruct"))
tokenizer = AutoTokenizer.from_pretrained(model_path("meta-llama/Meta-Llama-3-8B-Instruct"))

print(available_models())
```
