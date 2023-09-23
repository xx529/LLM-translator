from typing import Any, List, Mapping, Optional

import zhipuai
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM


class ZhiPuLLM(LLM):
    api_key: str
    model: str

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
            ]
        )
        c = response['data']['choices'][0]['content']
        return c

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {'api_key': self.api_key, 'model': self.model}
