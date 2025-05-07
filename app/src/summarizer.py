from openai import OpenAI
from config.settings import Settings

class Summarizer:
    def __init__(self, config: Settings):
        self.api_key = config.API_KEY
        self.base_url = config.BASE_URL
        self.model = config.MODEL
        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
        )

    def summarize(self, text: str, sumLen: str, sumQuality: str, lang: str) -> str:
        try:
            completion = self.client.chat.completions.create(
                model = self.model,
                messages=[
                    {
                        "role": "user",
                        "content": f"""
                        Summarize the following text in this language:{lang}.
                        Length of the summary:{sumLen}
                        Quality of the summary:{sumQuality}
                        Text to summarize:\n\n{text}"""
                    }
                ]
            )

            result = completion.choices[0].message.content

            return result

        except Exception as e:
            raise Exception(f"Summarization error: {str(e)}")