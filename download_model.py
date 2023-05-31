from transformers import AutoModelForSequenceClassification, AutoTokenizer

HUGGINGFACE_MODEL = 'facebook/bart-large-mnli'

# Load model and processor
AutoModelForSequenceClassification.from_pretrained(HUGGINGFACE_MODEL).save_pretrained('./model')
AutoTokenizer.from_pretrained(HUGGINGFACE_MODEL).save_pretrained('./model')