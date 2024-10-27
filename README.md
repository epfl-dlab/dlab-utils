# DLAB utils
Python Library for DLAB utils

## Installation

You can install the `dlabutils` package using pip:

```bash
pip install git+https://github.com/epfl-dlab/dlab-utils.git
```

## Usage

### Model Paths

To use the model path functionality, you can import the necessary functions from the `dlab-utils.paths` module. The `model_path` function returns the path to the model weights, if the model is available in the DLAB LLM weights directory, and defaults to the model name if it is not. The `available_models` function returns a list of all available models. Here's a quick tutorial:

```python
from dlab_utils.paths import model_path, available_models
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = model_path("meta-llama/Meta-Llama-3-8B-Instruct")
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

print(available_models())
```
