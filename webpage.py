import streamlit as st
from models import Model
from workers import Translator, Summarizer
from utils import Language, Log, FileReader
import streamlit_authenticator as stauth


def run():
    set_st()
    # user_login()

    run_app('test')


def set_st():
    st.set_page_config(layout="wide")

#
# def user_login():
#     config = FileReader.read_yaml('config.yaml')
#
#     authenticator = stauth.Authenticate(config['credentials'],
#                                         config['cookie']['name'],
#                                         config['cookie']['key'],
#                                         config['cookie']['expiry_days'],
#                                         config['preauthorized'])
#
#     authenticator.login('Login', 'main')
#     status = st.session_state.get("authentication_status", None)
#     Log.info(f'authentication status: {status}')
#
#     match status:
#         case True:
#             user_name = st.session_state['name']
#             print(st.session_state)
#             authenticator.logout('Logout', 'sidebar')
#         case False:
#             st.error('Username/password is incorrect')
#         case None:
#             st.error('Username/password is incorrect')


def login_status():
    return st.session_state.get("authentication_status", None)


def run_app(user_name):

    st.header(f'Hello "{user_name}"!')
    params = sider_bar()
    tabs = st.tabs(['Readme', 'Translation', 'Summary', 'Extraction', 'KnowledgeQA', 'ChatRoom'])

    with tabs[0]:
        app_readme(user_name=user_name)

    with tabs[1]:
        app_translation(model_name=params['model_name'])

    with tabs[2]:
        app_summary(model_name=params['model_name'])

    with tabs[3]:
        app_extraction()

    with tabs[4]:
        app_knowledge_qa()

    with tabs[5]:
        app_chatroom()


def sider_bar():
    params = {}

    with st.sidebar:
        st.markdown('## Configurations')

        st.markdown('### Model')
        params['model_name'] = st.selectbox('选择模型', Model.list(), label_visibility='collapsed')

        st.markdown('### Parameters')
        e1 = st.expander('Temperature')
        params['temp'] = e1.slider('Temperature', max_value=1.0, min_value=0.0, value=0.8, label_visibility='collapsed')

        e2 = st.expander('Top K')
        params['top_k'] = e2.slider('Top_K', max_value=100, min_value=0, value=20, label_visibility='collapsed')

        e3 = st.expander('Top P')
        params['top_p'] = e3.slider('Top_P', max_value=1.0, min_value=0.0, value=0.75, label_visibility='collapsed')

    return params


def app_translation(model_name):

    dst_lang = st.selectbox('目标语言', Language.list())
    Log.info(f'dst_lang: {dst_lang}')

    src_col, dst_col = st.columns(2)
    content = src_col.text_area('translation-content', placeholder='输入需要翻译的文本', height=250, label_visibility='collapsed')
    Log.info(f'content: {content}')

    if content:
        translator = Translator(model_name=model_name)
        result = translator(dst_lang=dst_lang, content=content)
        dst_col.text_area('translation', value=result, height=250, label_visibility='collapsed')


def app_summary(model_name):
    st.markdown('摘要文字长度')
    length = st.slider('summary-length', min_value=100, max_value=300, value=150, label_visibility='collapsed')
    Log.info(f'length: {length}')

    content = st.text_area('summary-content', placeholder='copy your content here', height=250, label_visibility='collapsed')
    if content:
        summarizer = Summarizer(model_name=model_name)
        with st.spinner('摘要生成中......'):
            result = summarizer(content=content, length=length)
            st.caption('摘要如下：')
            Log.info(f'result length: {len(result)}')
            st.text_area('summary-result', value=result, label_visibility='collapsed', height=200)


def app_knowledge_qa():
    st.text_area('背景知识材料', height=250)
    st.text_input('提问')
    st.markdown('这是回答')


def app_readme(user_name):
    st.markdown(f'Hello "{user_name}"!')
    st.markdown('Thanks for using this app!')


def app_extraction():
    st.text_area('extraction-content', placeholder='copy your content here', height=250, label_visibility='collapsed')
    # st.
    data = {'col1': [1, 2], 'col2': [3, 4]}


def app_chatroom():
    st.caption('waiting for development...')

