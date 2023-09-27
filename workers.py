from models import Model
from utils import Log
from langchain import PromptTemplate


class Worker:
    def __init__(self, model_name):
        self.model_name = model_name
        self.llm = Model[model_name].value

    def __call__(self, **kwargs):
        Log.info(f'using model "{self.model_name}"')

        p = PromptTemplate.from_template(self.get_template()).format(**kwargs)
        Log.info(f'prompt: {p}')

        res = self.llm(p)
        Log.info(f'response: {res}')
        return res

    def get_template(self):
        template_func = getattr(self, f'template_{self.model_name.lower()}', self.template_default)
        Log.info(f'using template "{template_func.__name__}"')
        return template_func()

    def template_default(self):
        raise NotImplementedError


class Translator(Worker):

    def __init__(self, model_name):
        super().__init__(model_name)

    def template_default(self):
        return '原文: {content}，请翻译成{dst_lang}: '

    @staticmethod
    def template_zhipu():
        return '现在你是一个翻译专家，根据给出的原文，给出对应的{dst_lang}翻译，原文: {content}，翻译: '


class Summarizer(Worker):

    def __init__(self, model_name):
        super().__init__(model_name)

    def template_default(self):
        return '用{length}个左右的文字为已下内容提取摘要: {content}，摘要：'
