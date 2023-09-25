import streamlit as st
from models import Model
from translator import Translator
from utils import Language, Log


def run():
    app_translator()


def app_translator():
    st.markdown('# Welcome to LLM-translator')

    col1, col2 = st.columns(2)

    dst_lang = col1.selectbox('目标语言', Language.list())
    Log.info(f'dst_lang: {dst_lang}')

    model_name = col2.selectbox('选择模型', Model.list())
    Log.info(f'model_name: {model_name}')

    content = st.text_area('原文', placeholder='输入需要翻译的文本')
    Log.info(f'content: {content}')

    if not content:
        st.stop()

    with st.spinner('正在翻译中...'):
        translator = Translator(model_name=model_name)
        result = translator(dst_lang=dst_lang, content=content)
        st.text_area('译文', value=result)
