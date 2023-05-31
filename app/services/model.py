import logging
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

class TextClassificationModel():
    def __init__(self, model, tokenizer):
        self.classifier = pipeline(
            "zero-shot-classification",
            model=model,
            tokenizer=tokenizer
        )

    def predict(self, text, candidate_labels: list[str]):
        results = self.classifier(text, candidate_labels, multi_label=True)

        logging.info(results)

        # Format results
        formatted_results = list()
        for index, label in enumerate(results["labels"]):
            formatted_results.append(
                {'label': label, 'score': results["scores"][index]*100}
            )

        return formatted_results

text_classification_model = TextClassificationModel(
    model=AutoModelForSequenceClassification.from_pretrained('./model'),
    tokenizer = AutoTokenizer.from_pretrained('./model')
)