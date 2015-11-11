# -*- coding: utf-8 -*-
"""
    skin.core
    ~~~~~~~~~

    There is where the management of the project template happens

    :copyright: (c) 2015 by the Leiser Fernández Gallo.
    :license: BSD License.
"""
from os import walk, mkdir, listdir, remove
from os.path import (relpath, join, expanduser, exists, split,
                     abspath, dirname, basename, isdir)
from shutil import copy, move
from _compat import Queue
from codecs import open


from templates import Template

_here = unicode(dirname(abspath(__file__)))
TEMPLATES_DIR = (expanduser(join(u'~', u'.skin')), join(_here, u'templates'))

_skins = None


def _skins2paths():
    global _skins
    if _skins:
        return _skins
    _skins = {}

    for td in TEMPLATES_DIR:
        if not exists(td):
            continue
        for d in listdir(td):
            d = abspath(join(td, d))
            if isdir(d):
                _skins[basename(d)] = d
    return _skins


def skin_path(name):
    """
    Find a skin in the skins folders and return a path to be rendered
    :param name: Name of the skin
    :type name: unicode
    :rtype: unicode
    """
    return _skins2paths()[name]


def list_skins():
    """
    List of skins name
    :rtype: list(unicode)
    """
    return list(_skins2paths())


def render(template_file, output_file, data):
    """
    Render a template file to another file

    :param template_file: file path to load the template
    :type template_file: unicode
    :param output_file: file path to the output
    :type output_file: unicode
    :param data: dict that map name to values for being used as
                 context of the templates
    :type data: dict
    """
    tmpl = Template.from_file(template_file)
    with open(output_file, mode='w', encoding='utf-8') as f:
        f.write(tmpl.render(data))


def loadvars(filepath):
    """
    Load visible vars from the rules file
    :param filepath: path to the file with the vars
    :type filepath: unicode
    :rtype: dict
    """
    if not exists(filepath):
        return {}

    import utils
    glob = {k: getattr(utils, k) for k in utils.RULES_UTILS}
    local = {}
    execfile(filepath, glob, local)
    return local


def render_skin(name, output_path):
    """
    Render a skin giving their name and the data to fill it in a giving path
    :param name: Name of the skin
    :type name: unicode
    :param data: dict that map name to values for being used as
                 context of the templates
    :type output_path: unicode
    """
    _skin_path = skin_path(name)
    to_rename = Queue()  # Copy first rename latter

    data = loadvars(join(_skin_path, 'skin_rules.py'))

    for root, folders, files in walk(_skin_path):
        rel = relpath(root, _skin_path)

        for file in files:
            file_input = join(root, file)
            file_output = join(output_path, rel, file)
            if file.endswith('.tmpl'):
                file_output = file_output[:-5]
                render(file_input, file_output, data)
            else:
                copy(file_input, file_output)
            to_rename.put(file_output)

        for folder in folders:
            folder_path = join(output_path, rel, folder)
            mkdir(folder_path)
            to_rename.put(folder_path)

    while not to_rename.empty():
        path = to_rename.get()
        head, tail = split(path)
        name = Template(tail).render(data)
        if name != tail:
            move(path, join(head, name))

    try:
        remove(join(output_path, 'skin_rules.py'))
    except OSError as e:
        import errno
        if e.errno != errno.ENOENT:
            raise
