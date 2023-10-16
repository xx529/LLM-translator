import loguru
import yaml


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


class FileReader:

    @classmethod
    def read(cls, path: str):
        if path.endswith('.yaml') or path.endswith('yml'):
            return cls.read_yaml(path)
        else:
            raise Exception('None supported file type')

    @staticmethod
    def read_yaml(path):
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)
