# API zero-shot text classification

This is a Python application built with FastAPI and Transformers that allows you to perform zero-shot text classification using a transformer-based model. It uses `facebook/bart-large-mnli` model from [Hugging Face](https://huggingface.co/facebook/bart-large-mnli).

## Getting Started

### Prerequisites

- Python 3.10

## Installation

1. Clone this repository to your local machine:
```
git clone https://github.com/yourusername/xxxxxxx.git
```

2. Create a python virtual env
```
python3 -m venv venv
```

3. Activate the virtual env
```
. venv/bin/activate
```

4. Install the dependencies
```
pip install -r requirements.txt
pip install -r requirements-dev.txt
pip install -r requirements-load-model.txt
```

5. Download model from HuggingFace
```
python ./download_model.py
```

## Usage

*⚠️ Unsure your virtual env is activate ⚠️*

### Lint
```
pylint app
```

### Test
```
pytest -o log_cli=true --log-cli-level=INFO
```

### Start locally

1. Start the FastAPI server:
```
uvicorn app.main:app --reload
```

2. Open your web browser and go to http://localhost:8000/docs to access the Swagger UI.

3. To classify the image with its input labels, send a POST request to the `/api/classify` endpoint with the following payload:
```json
{
    "labels": ["sport","politique","science"],
    "text": "L'équipe de France joue aujourd'hui au Parc des Princes"
}
```

The response will be a JSON object with the following structure:
```json
{
    "predictions": [
        {
            "label": "xxxx",
            "score": 95.54687354
        },
        {
            "label": "yyyy",
            "score": 1.234443184
        },
        {
            "label": "zzzz",
            "score": 3.908742123
        }
    ]
}
```

### Docker
```
docker build . -t api-text-classifier:0.0.1
```
```
docker run --name api-text-classifier --rm -d -p 8080:80 api-text-classifier:0.0.1
```