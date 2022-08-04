from time import time
from bot import DOWNLOAD_DIR, LOGGER
from bot.helper.ext_utils.bot_utils import get_readable_file_size, MirrorStatus, get_readable_time
from bot.helper.ext_utils.fs_utils import get_path_size


class SplitStatus:
    def __init__(self, name, size, gid, listener, message):
        self.__name = name
        self.__gid = gid
        self.__size = size
        self.__listener = listener
        self.__uid = listener.uid
        self.__start_time = time()
        self.message = listener.message
        self.message = message

    def progress(self):
        return '0'
        return f'{round(self.progress_raw(), 2)}%'

    def speed(self):
        return '0'
        return f'{get_readable_file_size(self.speed_raw())}/s'
    
    def size_raw(self):
        return self.__size
    
    def name(self):
        return self.__name

    def path(self):
        return self.__path
    def size_raw(self):
        return self.__size
    def size(self):
        return get_readable_file_size(self.__size)

    def eta(self):
        return '0s'
        try:
            seconds = (self.size_raw() - self.processed_bytes()) / self.speed_raw()
            return f'{get_readable_time(seconds)}'
        except:
            return '-'

    def status(self):
        return MirrorStatus.STATUS_SPLITTING

    def processed_bytes(self):
        return 0
