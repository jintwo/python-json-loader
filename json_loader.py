__version__ = '0.0.1'

import imp
import sys
import json
import os.path


class DictWrapper(dict):
    def __getattr__(self, item):
        return self.get(item)

    @classmethod
    def create(cls, d):
        res = cls()
        for k, v in d.items():
            res[k] = cls.create(v) if isinstance(v, dict) else v
        return res


def create_mod_wrapper(mod_path):
    m = sys.modules.setdefault(mod_path, imp.new_module(mod_path))
    m.__file__ = mod_path
    m.__package__ = mod_path
    return m


def module_from_dict(d, mod_path):
    m = create_mod_wrapper(mod_path)
    for k, v in d.items():
        if isinstance(v, dict):
            setattr(m, k, DictWrapper.create(v))
        else:
            setattr(m, k, v)
    return m


def create_json_mod_wrapper(mod_path, json_file):
    json_data = json.load(open(json_file))
    return module_from_dict(json_data, mod_path)


class JsonLoader(object):
    def __init__(self, json_file):
        self.json_file = json_file

    def load_module(self, fullname):
        if os.path.exists(self.json_file):
            m = create_json_mod_wrapper(fullname, self.json_file)
        else:
            m = create_mod_wrapper(fullname)
        m.__loader__ = self
        return m


class JsonFinder(object):
    def __init__(self, path):
        self.path = path

    def find_module(self, fullname, path=None):
        filename = os.path.join(self.path, '{}.json'.format(fullname))
        if os.path.exists(filename):
            return JsonLoader(filename)


def install_json_loader(path):
    sys.meta_path.append(JsonFinder(path))
