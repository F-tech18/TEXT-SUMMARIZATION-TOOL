from TransformerS import pipeline

class TextSummarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text, max_length=130, min_length=30, tone="formal"):
        summary = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )[0]['summary_text']

        if tone == "simple":
            summary = self._simplify_text(summary)

        return summary

    def bullet_summary(self, text):
        summary = self.summarize(text)
        sentences = summary.split('. ')
        bullets = [f"- {s.strip()}" for s in sentences if s]
        return "\n".join(bullets)

    def _simplify_text(self, text):
        return text.replace("however", "but").replace("therefore", "so")
