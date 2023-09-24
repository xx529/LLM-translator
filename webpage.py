import os
import streamlit as st
from model import ZhiPuLLM
from prompt import TranslatePrompt
from utils import Language, Log

chat_model = ZhiPuLLM(api_key=os.getenv('ZHIPUAI_API_KEY'),
                      model=os.getenv('ZHIPUAI_MODEL'))


def run():
    st.markdown('# Welcome to LLM-translator')

    dst_lang = st.selectbox('请选择需要翻译的语言', Language.list())
    Log.info(f'dst_lang: {dst_lang}')

    content = st.text_area('输入需要翻译的文本', placeholder='你好')
    Log.info(f'input: {content}')

    if not content:
        st.stop()

    with st.spinner('正在翻译中...'):
        prompt = TranslatePrompt.translate(dst_lang, content)
        result = chat_model(prompt)
        Log.info(f'translation: {result}')

    st.markdown(result)
