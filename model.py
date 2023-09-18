class Model:
    def chat(self, prompt):
        raise NotImplementedError("Subclasses should implement this!")


class ZhiPuAIModel(Model):

    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model

    def chat(self, prompt):
        import zhipuai
        zhipuai.api_key = self.api_key
        response = zhipuai.model_api.invoke(
            model=self.model,
            prompt=[
                {"role": "user", "content": prompt},
            ]
        )
        c = response['data']['choices'][0]['content']
        return c
