import loguru
from enum import Enum


class Log:
    log = loguru.logger

    @classmethod
    def info(cls, msg):
        cls.log.info(msg)

    @classmethod
    def debug(cls, msg):
        cls.log.debug(msg)

    @classmethod
    def warning(cls, msg):
        cls.log.warning(msg)

    @classmethod
    def error(cls, msg):
        cls.log.error(msg)

    @classmethod
    def critical(cls, msg):
        cls.log.critical(msg)

    @classmethod
    def exception(cls, msg):
        cls.log.exception(msg)


class Language(Enum):
    Chinese = '中文'
    English = '英语'
    Korean = '韩语'
    Russian = '俄语'
    Cantonese = '粤语'
    French = '法语'
    Japanese = '日语'
    Spanish = '西班牙语'
    Portuguese = '葡萄牙语'

    @classmethod
    def list(cls):
        return [lang.value for lang in cls]
