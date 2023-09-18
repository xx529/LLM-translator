import os
from model import ZhiPuAIModel
from prompt import TranslatePrompt

if __name__ == '__main__':
    m = ZhiPuAIModel(os.getenv('ZHIPUAI_API_KEY'), os.getenv('ZHIPUAI_MODEL'))

    prompt = TranslatePrompt.prompt('英语', '法语', '今天星期几')

    print(m.chat(prompt))
