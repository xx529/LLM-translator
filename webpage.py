import os
import streamlit as st
from models import Model
from prompt import TranslatePrompt
from translator import Translator
from utils import Language, Log


def run():
    st.markdown('# Welcome to LLM-translator')

    dst_lang = st.selectbox('请选择需要翻译的语言', Language.list())
    Log.info(f'dst_lang: {dst_lang}')

    model_name = st.selectbox('请选择模型', [model.name for model in Model])
    Log.info(f'model_name: {model_name}')

    content = st.text_area('输入需要翻译的文本', placeholder='你好')
    Log.info(f'input: {content}')

    if not content:
        st.stop()

    with st.spinner('正在翻译中...'):
        translator = Translator(model_name=model_name)
        result = translator(dst_lang=dst_lang, content=content)
        Log.info(f'translation: {result}')

    st.markdown(result)
