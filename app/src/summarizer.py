from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import (
    TextAnalyticsClient,
    ExtractiveSummaryAction
)
from config.settings import Settings

class Summarizer:
    def __init__(self, config: Settings):
        self.endpoint = config.AZURE_ENDPOINT
        self.key = config.AZURE_API_KEY
        self.client = TextAnalyticsClient(
            endpoint=self.endpoint,
            credential=AzureKeyCredential(self.key)
        )

    def summarize(self, text: str) -> str:
        try:
            actions = [
                ExtractiveSummaryAction(
                    max_sentence_count=5,
                    order_by="Rank"
                )
            ]

            poller = self.client.begin_analyze_actions(
                documents=[text],
                actions=actions,
                language="pl",
                show_stats=True
            )

            results = list(poller.result())

            summary_sentences = []
            for result in results:
                for action_result in result:
                    if not action_result.is_error:
                        summary_sentences.extend(
                            sentence.text for sentence in action_result.sentences
                        )

            return " ".join(summary_sentences) if summary_sentences else "No summary generated"

        except Exception as e:
            raise Exception(f"Summarization error: {str(e)}")