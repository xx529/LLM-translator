from utils import Log


class TranslatePrompt:

    @classmethod
    def prompt(cls, src_lang, dst_lang, content):
        _prompt = f"""
            {src_lang}: {content}
            {dst_lang}: 
            """
        Log.info(_prompt)
        return _prompt
