import streamlit as st
from models import Model
from translator import Translator
from utils import Language, Log


def run():
    st.header('Have Fun!')

    params = sider_bar()
    tabs = st.tabs(['Translator', 'KnowledgeQA', 'Extraction', 'ChatRoom', 'About'])

    with tabs[0]:
        app_translator(model_name=params['model_name'])

    with tabs[1]:
        app_knowledge_qa()

    with tabs[2]:
        app_chatroom()

    with tabs[3]:
        app_chatroom()

    with tabs[4]:
        app_about()


def sider_bar():
    params = {}

    st.sidebar.subheader('Select Model')
    params['model_name'] = st.sidebar.selectbox('选择模型', Model.list(), label_visibility='collapsed')

    st.sidebar.subheader('Temperature')
    params['temp'] = st.sidebar.slider('模型温度', max_value=1.0, min_value=0.0, value=0.8, label_visibility='collapsed')

    st.sidebar.subheader('Top K')
    params['top_k'] = st.sidebar.slider('Top K', max_value=100, min_value=0, value=0, label_visibility='collapsed')

    st.sidebar.subheader('Top P')
    params['top_p'] = st.sidebar.slider('Top P', max_value=1.0, min_value=0.0, value=0.75, label_visibility='collapsed')
    return params


def app_translator(model_name):

    dst_lang = st.selectbox('目标语言', Language.list())
    Log.info(f'dst_lang: {dst_lang}')

    src_col, dst_col = st.columns(2)
    content = src_col.text_area('原文', placeholder='输入需要翻译的文本', height=250, label_visibility='collapsed')
    Log.info(f'content: {content}')

    if not content:
        result = ''
    else:
        translator = Translator(model_name=model_name)
        result = translator(dst_lang=dst_lang, content=content)

    dst_col.text_area('译文', value=result, height=250, label_visibility='collapsed', disabled=True)


def app_knowledge_qa():
    st.text_area('背景知识材料', height=250)
    st.text_input('提问')
    st.markdown('这是回答')


def app_about():
    st.header('About')


def app_extraction():
    st.caption('waiting for development...')


def app_chatroom():
    st.caption('waiting for development...')
