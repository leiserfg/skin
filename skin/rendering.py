# -*- coding: utf-8 -*-
from __future__ import print_function
import datetime
from fnmatch import fnmatch
from functools import reduce
import os
import re

import jinja2

from ._compat import to_unicode
from .utils import prompt_bool
from .helpers import (pformat, make_dirs, create_file, copy_file, unormalize,
                      file_has_this_content, files_are_identical)
from posixpath import join as posix_join

DEFAULT_DATA = {
    'now': datetime.datetime.utcnow,
}

DEFAULT_FILTER = ('.*', '~*', '*.py[co]')
DEFAULT_INCLUDE = ()

DEFAULT_ENV_OPTIONS = {
    'autoescape': True,
    'block_start_string': '[%',
    'block_end_string': '%]',
    'variable_start_string': '[[',
    'variable_end_string': ']]',
}


def render_skeleton(src_path, dst_path, data=None,
                    filter_this=None, include_this=None,
                    pretend=False, force=False, skip=False, quiet=False,
                    envops=None):
    """
    src_path:
        Absolute path to the project skeleton

    dst_path:
        Absolute path to where to render the skeleton

    data:
        Data to be passed to the templates, as context.

    filter_this:
        A list of names or shell-style patterns matching files or folders
        that musn't be copied. The default is: ``['.*', '~*', '*.py[co]']``

    include_this:
        A list of names or shell-style patterns matching files or folders that
        must be included, even if its name are in the `filter_this` list.
        Eg: ``['.gitignore']``. The default is an empty list.

    pretend:
        Run but do not make any changes

    force:
        Overwrite files that already exist, without asking

    skip:
        Skip files that already exist, without asking

    quiet:
        Suppress the status output

    envops:
        Extra options for the Jinja template environment.

    """
    src_path = to_unicode(src_path)
    data = clean_data(data)
    data.setdefault('name', os.path.basename(dst_path))
    must_filter = get_name_filter(filter_this, include_this)
    render_tmpl = get_jinja_renderer(src_path, data, envops)

    for folder, subs, files in os.walk(src_path):
        rel_folder = folder.replace(src_path, '').lstrip(os.path.sep)
        if must_filter(rel_folder):
            continue
        for name in files:
            rel_path = os.path.join(rel_folder, re.sub(r'\.tmpl$', '', name))
            if must_filter(rel_path):
                continue
            render_file(dst_path, rel_folder, folder, name, render_tmpl,
                        pretend=pretend, force=force, skip=skip, quiet=quiet)


def clean_data(data):
    data = data or {}
    _data = DEFAULT_DATA.copy()
    _data.update(data)
    return _data

def path_chunk(path):
    chunks = []
    head = path
    while  True:
        head, tail = os.path.split(head)
        if tail == '':
            chunks.append(head)
            break
        chunks.append(tail)
    return reversed(chunks)


def get_jinja_renderer(src_path, data, envops=None):
    """Returns a function that can render a Jinja template.
    """
    envops = envops or {}
    _envops = DEFAULT_ENV_OPTIONS.copy()
    _envops.update(envops)
    _envops.setdefault('loader',
                       jinja2.FileSystemLoader(src_path, encoding='utf8'))
    env = jinja2.Environment(**_envops)

    def render_tmpl(fullpath):
        relpath = fullpath.replace(src_path, '').lstrip(os.path.sep)

        chunks = path_chunk(relpath)
        relpath = posix_join(*chunks)
       
        tmpl = env.get_template(relpath)
        return tmpl.render(data)

    return render_tmpl


def get_name_filter(filter_this, include_this):
    """Returns a function that evaluates if a file or folder name must be
    filtered out.

    The compared paths are first converted to unicode and decomposed.
    This is neccesary because the way PY2.* `os.walk` read unicode
    paths in different filesystems. For instance, in OSX, it returns a
    decomposed unicode string. In those systems, u'ñ' is read as `\u0303`
    instead of `\xf1`.
    """
    filter_this = [unormalize(to_unicode(f)) for f in
                   filter_this or DEFAULT_FILTER]
    include_this = [unormalize(to_unicode(f)) for f in
                    include_this or DEFAULT_INCLUDE]

    def fullmatch(path, pattern):
        path = unormalize(path)
        name = os.path.basename(path)
        return fnmatch(name, pattern) or fnmatch(path, pattern)

    def must_be_filtered(name):
        return reduce(lambda r, pattern: r or
                      fullmatch(name, pattern), filter_this, False)

    def must_be_included(name):
        return reduce(lambda r, pattern: r or
                      fullmatch(name, pattern), include_this, False)

    def must_filter(path):
        return must_be_filtered(path) and not must_be_included(path)

    return must_filter


def render_file(dst_path, rel_folder, folder, src_name, render_tmpl,
                pretend=False, force=False, skip=False, quiet=False):
    """Process or copy a file of the skeleton.
    """
    fullpath = os.path.join(folder, src_name)
    dst_name = re.sub(r'\.tmpl$', '', src_name)
    created_path = os.path.join(rel_folder, dst_name).lstrip('.').lstrip('/')

    if pretend:
        final_path = os.path.join(dst_path, rel_folder, dst_name)
    else:
        final_path = make_dirs(dst_path, rel_folder, dst_name)

    if not os.path.exists(final_path):
        if not quiet:
            pformat('create', created_path, color='green')
        if not pretend:
            make_file(src_name, render_tmpl, fullpath, final_path)
        return

    ## A file with this name already exists

    content = None
    if src_name.endswith('.tmpl'):
        content = render_tmpl(fullpath)
        identical = file_has_this_content(final_path, content)
    else:
        identical = files_are_identical(fullpath, final_path)

    # The existing file is identical.
    if identical:
        if not quiet:
            pformat('identical', created_path, color='cyan', bright=None)
        return

    # The existing file is different.
    if not quiet:
        pformat('conflict', created_path, color='red')
    if force:
        overwrite = True
    elif skip:
        overwrite = False
    else:
        msg = '  Overwrite %s? (y/n)' % final_path
        overwrite = prompt_bool(msg, default=True)

    if not quiet:
        pformat('force' if overwrite else 'skip', created_path, color='yellow')

    if overwrite and not pretend:
        if content is None:
            copy_file(fullpath, final_path)
        else:
            create_file(final_path, content)


def make_file(src_name, render_tmpl, fullpath, final_path):
    if src_name.endswith('.tmpl'):
        content = render_tmpl(fullpath)
        create_file(final_path, content)
    else:
        copy_file(fullpath, final_path)

