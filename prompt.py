from utils import Log
from langchain.prompts import PromptTemplate


class TranslatePrompt:

    @classmethod
    def translate(cls, dst_lang, content):
        _prompt = '现在你是一个翻译专家，根据给出的原文，给出对应的{dst_lang}翻译，原文: {content}，翻译: '
        p = PromptTemplate.from_template(_prompt).format(dst_lang=dst_lang, content=content)
        Log.info(p)
        return p

