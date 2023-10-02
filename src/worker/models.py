from typing import Any, List, Mapping, Optional
from enum import Enum
import os

import zhipuai
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM


class Faker(LLM):
    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(self,
              prompt: str,
              stop: Optional[List[str]] = None,
              run_manager: Optional[CallbackManagerForLLMRun] = None,
              **kwargs: Any) -> str:
        return 'I am a faker.'


class ZhiPuLLM(LLM):
    model: str
    api_key: str
    default_temperature: float = 0.9
    default_top_k: float = 10

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(self,
              prompt: str,
              stop: Optional[List[str]] = None,
              run_manager: Optional[CallbackManagerForLLMRun] = None,
              **kwargs: Any) -> str:

        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")

        zhipuai.api_key = self.api_key
        response = zhipuai.model_api.invoke(
            model=self.model,
            prompt=[
                {"role": "user", "content": prompt},
            ],
            temperature=kwargs.get('temperature', self.default_temperature),
            top_k=kwargs.get('top_k', self.default_top_k)
        )
        c = response['data']['choices'][0]['content']
        return c

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {'api_key': self.api_key, 'model': self.model}


class ChatGLM2(LLM):
    host: str
    port: str

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(self,
              prompt: str,
              stop: Optional[List[str]] = None,
              run_manager: Optional[CallbackManagerForLLMRun] = None,
              **kwargs: Any) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        return 'not implemented yet.'

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {'host': self.host, 'port': self.port}


class Model(Enum):
    ZhiPu = ZhiPuLLM(api_key=os.getenv('ZHIPUAI_API_KEY', ''), model=os.getenv('ZHIPUAI_MODEL', ''))
    ChatGLM_2 = ChatGLM2(host=os.getenv('GLM2_HOST', ''), port=os.getenv('GLM2_PORT', ''))
    Faker = Faker()

    @classmethod
    def list(cls):
        return [m.name for m in cls]
