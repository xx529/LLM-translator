import os
import streamlit as st
from model import ZhiPuLLM
from prompt import TranslatePrompt
from utils import LanguageChecker, Language, Log

# chat_model = ZhiPuAIModel(os.getenv('ZHIPUAI_API_KEY'), os.getenv('ZHIPUAI_MODEL'))
chat_model = ZhiPuLLM(api_key=os.getenv('ZHIPUAI_API_KEY'),
                      model=os.getenv('ZHIPUAI_MODEL'))


def run():
    st.markdown('# Welcome to LLM-translator')

    content = st.text_input('输入需要翻译的中文', value='你好', placeholder='输入需要翻译的中文')
    Log.info(f'input: {content}')
    if LanguageChecker.detect(content) != Language.Chinese.value:
        result = '您输入的不是中文，请重新输入！'
    else:
        with st.spinner('正在翻译中...'):
            prompt = TranslatePrompt.prompt('中文', '英文', content)
            result = chat_model(prompt)

    st.markdown(result)
