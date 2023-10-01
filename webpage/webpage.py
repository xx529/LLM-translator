import streamlit as st
from worker.models import Model
from worker.workers import Translator, Summarizer
from utils.tools import Log
from utils.types import Language, ModelConf


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
    conf = sider_bar()
    tabs = st.tabs(['Readme', 'Translation', 'Summary', 'Extraction', 'KnowledgeQA', 'ChatRoom'])

    with tabs[0]:
        app_readme(user_name=user_name)

    with tabs[1]:
        app_translation(conf=conf)

    with tabs[2]:
        app_summary(conf=conf)

    with tabs[3]:
        app_extraction()

    with tabs[4]:
        app_knowledge_qa()

    with tabs[5]:
        app_chatroom()


def sider_bar() -> ModelConf:

    with st.sidebar:
        st.markdown('## Configurations')

        st.markdown('### Model')
        model_name = st.selectbox('选择模型', Model.list(), label_visibility='collapsed')
        llm_model = Model[model_name].value

        conf = ModelConf(llm_model=Model[model_name].value)

        st.markdown('### Parameters')

        if hasattr(llm_model, 'default_temperature'):
            e1 = st.expander('Temperature')
            conf.temperature = e1.slider(label='Temperature',
                                         value=llm_model.default_temperature,
                                         max_value=1.0, min_value=0.0, label_visibility='collapsed')

        if hasattr(llm_model, 'default_top_k'):
            e2 = st.expander('Top K')
            conf.top_k = e2.slider(label='Top_K',
                                   value=llm_model.default_top_k,
                                   max_value=50, min_value=0, label_visibility='collapsed')

        if hasattr(llm_model, 'default_top_p'):
            e3 = st.expander('Top P')
            conf.top_p = e3.slider(label='Top_P',
                                   value=llm_model.default_top_p,
                                   max_value=1.0, min_value=0.0, label_visibility='collapsed')

    return conf


def app_translation(conf: ModelConf):

    dst_lang = st.selectbox('目标语言', Language.list())
    Log.info(f'dst_lang: {dst_lang}')

    src_col, dst_col = st.columns(2)
    content = src_col.text_area('translation-content', placeholder='输入需要翻译的文本', height=250, label_visibility='collapsed')
    Log.info(f'content: {content}')

    if content:
        translator = Translator(llm_model=conf.llm_model,
                                temperature=conf.temperature,
                                top_k=conf.top_k,
                                top_p=conf.top_p)

        result = translator(dst_lang=dst_lang, content=content)
        dst_col.text_area('translation', value=result, height=250, label_visibility='collapsed')


def app_summary(conf: ModelConf):
    st.markdown('摘要文字长度')
    length = st.slider('summary-length', min_value=100, max_value=300, value=150, label_visibility='collapsed')
    Log.info(f'length: {length}')

    content = st.text_area('summary-content', placeholder='copy your content here', height=250, label_visibility='collapsed')
    if content:
        summarizer = Summarizer(llm_model=conf.llm_model,
                                temperature=conf.temperature,
                                top_k=conf.top_k,
                                top_p=conf.top_p)

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
    # data = {'col1': [1, 2], 'col2': [3, 4]}


def app_chatroom():
    st.caption('waiting for development...')

