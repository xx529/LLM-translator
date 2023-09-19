import os
import streamlit as st
from model import ZhiPuAIModel
from prompt import TranslatePrompt

m = ZhiPuAIModel(os.getenv('ZHIPUAI_API_KEY'), os.getenv('ZHIPUAI_MODEL'))


def run():
    st.markdown('# Welcome to LLM-translator')

    content = st.text_input('输入需要翻译的中文', value='你好', placeholder='输入需要翻译的中文')

    prompt = TranslatePrompt.prompt('中文', '英文', content)

    with st.spinner('正在翻译中...'):
        result = m.chat(prompt)

    st.markdown(result)
