import loguru
import langdetect
from enum import Enum
from langdetect import DetectorFactory

DetectorFactory.seed = 0


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


class LanguageChecker:

    @staticmethod
    def detect(text):
        lang = langdetect.detect_langs(text)
        Log.info(f"Detected language: {lang}")
        return lang[0].lang


class Language(Enum):
    Chinese = 'zh-cn'
    English = 'en'
