import getpass
import time
from sys import platform
from threading import Thread

from pytube import YouTube


class Download:
    def __download_video(self, html, num):
        time.sleep(2)
        if platform == "linux" or platform == 'linux2':
            full_path = '/home/' + getpass.getuser() + '/TubeDownloader'
            a = YouTube(html)
            a.streams.first().download(full_path)
        elif platform == "win32":
            path = 'C:\\Documents and Settings\\'
            full_path = path + getpass.getuser() + '\\TubeDownloader'
            a = YouTube(html)
            a.streams.first().download(full_path)

    def download(self, links, thread=False):
        for num, i in enumerate(links):
            if thread is True:
                mtTh = Thread(target=self.__download_video, args=(i, num))
                mtTh.start()
            else:
                try:
                    self.__download_video(i, num)
                except Exception as e:
                    if 'regex pattern' in str(e):
                        return 'Error in link'
