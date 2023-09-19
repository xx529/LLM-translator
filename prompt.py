from utils import Log


class TranslatePrompt:

    @classmethod
    def prompt(cls, src_lang, dst_lang, content):
        _prompt = f"""
            现在你需要将一段{src_lang}句子翻译成{dst_lang}，你需要根据一下步骤一步一歩来
            
            1. 如何句子是{src_lang}之外的语言，如果不是请回答："输入的句子不是{src_lang}"
            2. 请将其翻译成{dst_lang}，并回答："翻译结果：xxx"
            
            以下是句子：
            {content}
            """
        Log.info(_prompt)
        return _prompt
