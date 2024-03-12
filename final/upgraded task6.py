import logging
import os
import argparse
from collections import namedtuple
# from sys import platform


def parser():
    parser = argparse.ArgumentParser(description='Our parser')
    parser.add_argument('folder', metavar='F', type=str, nargs='*', help='Please, enter folder path.')
    args = parser.parse_args()
    print(args.folder[0])
    create_namedtuple(args.folder[0])


def log(folder_object):
    FORMAT = '{levelname:<8} - {asctime}. {msg}'
    logging.basicConfig(filename='folder_object.log', format=FORMAT, style='{', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(f'Append\t{folder_object}')


def create_namedtuple(folder):
    # список полей класса
    fields = ['name', 'ext', 'flag_folder', 'parent_folder']
    # создаётся класс FolderObject
    FolderObject = namedtuple('FolderObject', fields)
    # список FolderObject (содержимое folder)
    content_list = []
    if os.path.exists(folder):
        folder_content = os.walk(folder)
        for path, folders, files in folder_content:
            # print(f'{path = } ___ {folders = } ___ {files = }')
            parent_folder = path.rsplit('\\', 1)[-1]
            for item in folders:
                folder_object = FolderObject(item, None, True, parent_folder)
                content_list.append(folder_object)
                log(folder_object)
            for item in files:
                # если файл оказался без расширения
                try:
                    file_name, file_ext = item.rsplit('.', 1)
                except ValueError:
                    file_name = item
                    file_ext = 'absent'
                folder_object = FolderObject(file_name, file_ext, False, parent_folder)
                content_list.append(folder_object)
                log(folder_object)
        print(*content_list)
    else:
        print(f'Директории {folder} не существует!')


if __name__ == '__main__':
     folder = 'C:\\Users\\Михаил\\Desktop\\экз'
     create_namedtuple(folder)
     parser()