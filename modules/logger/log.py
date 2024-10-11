try:
    import logging
    import os
    from sys import exit
except ImportError:
    print("Ошибка подключения модуля(библиотеки)")
    exit()

core_dir = (os.path.abspath(os.curdir))

def create_logfile() -> str:
    path_log_file = os.path.join(core_dir, "log","application.log")
    
    if os.path.exists(path_log_file) is False:
        try:
            os.makedirs(os.path.join(core_dir, "log"), exist_ok=True)
            log_file = open(path_log_file, "w+")
            log_file.close
        except Exception as e:
            print(f"Ошибка создания файла журналирования. ({e})")
            exit(1)
    return path_log_file
    
logger = logging.getLogger('application-log')

formatter = logging.Formatter(
    "%(asctime)s (%(filename)s).(%(funcName)s).(%(lineno)d) - %(message)s"
)

all_handler = logging.FileHandler(create_logfile())
all_handler.setLevel(logging.DEBUG)
all_handler.setFormatter(formatter)

logger.addHandler(all_handler)