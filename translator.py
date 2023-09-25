from models import Model
from utils import Log
from langchain import PromptTemplate


class Translator:

    def __init__(self, model_name):
        self.model_name = model_name
        self.llm = Model[model_name].value

    def __call__(self, dst_lang, content):
        Log.info(f'using model "{self.model_name}"')
        p = PromptTemplate.from_template(self.prompt_general()).format(dst_lang=dst_lang, content=content)
        Log.info(f'prompt: {p}')
        return self.llm(p)

    @staticmethod
    def prompt_general():
        return '现在你是一个翻译专家，根据给出的原文，给出对应的{dst_lang}翻译，原文: {content}，翻译: '

    def prompt_zhipu(self):
        return self.prompt_general()
