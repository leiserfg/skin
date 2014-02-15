from os.path import expanduser, join, abspath, dirname, basename, isdir, exists
from os import chdir, listdir, getcwdu, walk, rename as os_rename
from jinja2 import Template

from rendering import render_skeleton
import utils
from helpers import pformat

_here = unicode(dirname(abspath(__file__)))

_templates_dirs = (expanduser(join(u'~', u'.skin')), join(_here, u'templates'))


def template_path(name):
    "Return the path of a template by name"
    for td in _templates_dirs:
        if not exists(td): continue
        for d in listdir(td):
            d = abspath(join(td, d))
            if name == basename(d) and isdir(d):
                return d
    raise Exception('Template %s does not exist' % name)

def templates():
    """
    Return a iterator over the templates names, we use a set internally for avoiding 
    the duplication of names.
    """
    tmpls = set() 
    for td in _templates_dirs:
        if not exists(td): continue
        for d in listdir(td):
            d = abspath(join(td, d))
            if isdir(d):
                tmpls.add(basename(d))
    return iter(tmpls)


def get_rules(rules_path):
    post_render =  lambda :None
    data = {}
    if exists(rules_path):
        pformat('getting rules', color='blue')
        local = {k:getattr(utils, k) for k in utils.__all__ if k != '__all__'}
        glob = {}
        execfile(rules_path, glob, local)
        post_render = local.get('post_render', post_render)
        data = local.get('data', data)
    return data, post_render

def clean():
    if exists("skin_rules"):
        utils.rm("skin_rules")

def rename(data, src_path, dest_path):
    for root, folders, files in walk(src_path):
        for f in folders + files:
            if f.endswith('.tmpl'): f = f[:-5]
            old_fullpath = join(dest_path, f)
            tmpl = Template(f)
            new_path = tmpl.render(**data)
            if f != new_path:
                os_rename(old_fullpath, new_path)
                pformat('rename', ' '.join([old_fullpath, 'to', new_path]), 
                        color='green')


def render(name):
    tmpl_path = template_path(name)
    out_path = getcwdu()
    data, post_render = get_rules(join(tmpl_path, 'skin_rules'))
    render_skeleton(tmpl_path, out_path, data=data)
    rename(data, tmpl_path, out_path)
    post_render()
    clean()




