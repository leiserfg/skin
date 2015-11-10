# -*- coding: utf-8 -*-
"""
    skin.core
    ~~~~~~~~~

    There is where the management of the project template happens

    Little modifications to werkzeug.templates

    :copyright: (c) 2015 by the Leiser Fernández Gallo.
    :license: BSD License.
"""
from os import walk, mkdir
from os.path import relpath, join, split
from shutil import copy, move
from _compat import Queue
from codecs import open

from templates import Template


def skin_path_from_name(name):
    """
    Find a skin in the skins folders and return a path to be rendered
    :param name: Name of the skin
    :type name: unicode
    :rtype: unicode
    """
    # TODO
    pass


def render(file_input, file_output, data):
    tmpl = Template.from_file(file_input)
    with open(file_output, mode='w', encoding='utf-8') as f:
        f.write(tmpl.render(data))


def render_skin(name, data, output_path):
    """
    Render a skin giving their name and the data to fill it in a giving path
    :param name: Name of the skin
    :type name: unicode
    :param data: dict that map name to values for being used as context of 
                 the templates
    :type data: dict
    :param output_path: absolute path to write the rendered skin
    :type output_path: unicode
    """
    skin_path = skin_path_from_name(name)
    torename = Queue()

    for root, folders, files in walk(skin_path):
        rel = relpath(root, skin_path)

        for topfile in files:
            file_input = join(root, file)
            file_output = join(output_path, rel, file[:-5])
            if file.endswith('.tmpl'):
                render(file_input, file_output, data)
            else:
                copy(file_input, file_output)
            torename.put(file_output)

        for folder in folders:
            folder_path = join(output_path, rel, folder)
            mkdir(folder_path)
            torename.put(folder_path)

    while not torename.empty():
        thing = torename.get()
        dirname, basename = split(thing)
        basename = Template(basename).render(data)
        move(thing, join(dirname, basename))

