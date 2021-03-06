import pybars
from utils.log import get_logger
from utils.config import get_config

logger = get_logger(__name__)


def compile(folder: str, file_name: str, data: dict) -> str:
    file_path = '%s/%s/%s' % (get_config()
                              ['environmet']['templateFolder'], folder, file_name)

    logger.debug('Retrieving template from file [%s]' % (file_path))
    compiler = pybars.Compiler()
    file = open(file_path, 'r', encoding="utf-8")
    file_string = file.read()
    template = compiler.compile(file_string)
    final_string = template(data)
    if (get_config()['environmet']['printXml']):
        logger.debug('Compiled template [%s]' % (final_string))
    return final_string


logger.info("Module [template] started correctly")
