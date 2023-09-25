from models import Model
from utils import Log
from langchain import PromptTemplate


class Translator:

    def __init__(self, model_name):
        self.model_name = model_name
        self.llm = Model[model_name].value

    def __call__(self, dst_lang, content):
        Log.info(f'using model "{self.model_name}"')

        p = PromptTemplate.from_template(self.get_template()).format(dst_lang=dst_lang, content=content)
        Log.info(f'prompt: {p}')

        res = self.llm(p)
        Log.info(f'response: {res}')
        return res

    def get_template(self):
        template_func = getattr(self, f'template_{self.model_name.lower()}', self.template_default)
        Log.info(f'using template "{template_func.__name__}"')
        return template_func()

    @staticmethod
    def template_default():
        return '原文: {content}，请翻译成{dst_lang}: '

    @staticmethod
    def template_zhipu():
        return '现在你是一个翻译专家，根据给出的原文，给出对应的{dst_lang}翻译，原文: {content}，翻译: '
