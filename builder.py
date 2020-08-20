"""Build Process
"""
import sys
import json
import os
import stat
import subprocess
import shutil
import re
import datetime


class Builder(object):
    """Builds the abstract python package based on the open-traffic-generator 
    models repository.
    """
    def __init__(self, dependencies=True, clone_and_build=True):
        self.__python = os.path.normpath(sys.executable)
        self.__python_dir = os.path.dirname(self.__python)
        self._src_dir = './abstract_open_traffic_generator'
        self._dependencies = dependencies
        self._clone_and_build = clone_and_build
        self._install_dependencies()
        self._clone_models_and_build()

    def _install_dependencies(self):
        if self._dependencies is False:
            return
        packages = [
            'pyyaml', 
            'jsonpath-ng'
        ]
        for package in packages:
            print('installing dependency %s...' % package)
            process_args = [
                self.__python,
                '-m',
                'pip',
                'install',
                '-U',
                package
            ]
            subprocess.Popen(process_args, shell=False).wait()

    def _handleError(self, func, path, exc_info):
        if not os.access(path, os.W_OK):
            try:
                os.chmod(path, stat.S_IWUSR)
                func(path)
            except Exception as e:
                print(e)

    def _clone_models_and_build(self):
        if self._clone_and_build is False:
            return
        print('cloning models...')
        shutil.rmtree('./models', onerror=self._handleError)
        if os.path.exists('./models') is True:
            os.rmdir('./models')
        process_args = [
            'git',
            'clone',
            'https://github.com/open-traffic-generator/models.git',
        ]
        process = subprocess.Popen(process_args, shell=False)
        process.wait()
        process_args = [
            'python',
            'bundler.py'
        ]
        subprocess.Popen(process_args, cwd='./models', shell=False).wait()

    def generate(self):
        shutil.rmtree(self._src_dir, onerror=self._handleError)
        if os.path.exists(self._src_dir) is True:
            os.rmdir(self._src_dir)
        with open('./models/openapi.yaml') as fid:
            self._openapi =  yaml.safe_load(fid)
        os.mkdir(self._src_dir)
        self._write_data_class()

    def _write_data_class(self):
        for key, yobject in self._openapi['components']['schemas'].items():
            pieces = key.split('.')
            self._classname = key
            path = self._src_dir + '/'
            if '.' in key:
                self._classname = pieces[-1]
                path += '_'.join(pieces[0:-1]).lower()
            self._classfilename = path
            print('generating %s in file %s...' % (self._classname, self._classfilename))

            with open(self._classfilename + '.py', 'a') as self._fid:
                self._write()
                self._write()
                self._write(0, 'class %s(object):' % self._classname)
                
                # class documentation
                self._write(1, '"""%s class' % key)
                self._write()
                if 'description' not in yobject:
                    yobject['description'] = 'TBD'
                # remove tabs, double spaces
                description = re.sub('\n|\t|\s|\s+', ' ', yobject['description'])
                for line in description.split('-'):
                    self._write(1, '%s' % line)
                self._write()
                self._write(1, "Args")
                self._write(1, "----")
                for name, property in yobject['properties'].items():
                    if 'description' not in property:
                        property['description'] = 'TBD'
                    type = self._get_type_restriction(property)
                    self._write(1, "- %s (%s): %s" % (name, type, property['description'].replace('\n', ' ')))
                self._write(1, '"""')

                # constants
                if 'x-constants' in yobject.keys():
                    self._write(1)
                    for constant, value in yobject['x-constants'].items():
                        self._write(1, "%s = '%s'" % (constant.upper(), value))
                    self._write(1)

                args = ''
                choice_tuples = []
                for name, property in yobject['properties'].items():
                    args += '%s%s=None' % (', ', name) 
                    if name == 'choice':
                        for choice_enum in property['enum']:
                            choice = yobject['properties'][choice_enum]
                            if '$ref' in choice:
                                choice_classname = self._get_classname_from_ref(choice['$ref'])
                                choice_tuples.append((choice_classname, choice_enum, choice['$ref']))
                            elif choice['type'] == 'string':
                                choice_tuples.append(('str', choice_enum, None))
                            elif choice['type'] in ['number', 'integer']:
                                choice_tuples.append(('float', choice_enum, None))
                                choice_tuples.append(('int', choice_enum, None))
                            elif choice['type'] == 'array':
                                choice_tuples.append(('list', choice_enum, None))
                if len(choice_tuples) > 0:
                    args = ', choice'
                    self._write(1, '_CHOICE_MAP = {')
                    for choice_tuple in choice_tuples:
                        self._write(2, "'%s': '%s'," % (choice_tuple[0], choice_tuple[1]))
                    self._write(1, '}')
                self._write(1, 'def __init__(self%s):' % args)
                self._write_data_properties(yobject, self._classname, choice_tuples)
        return self

    def _write_data_properties(self, schema, classname, choice_tuples):
        import_lines = []
        if len(choice_tuples) > 0:
            for choice_tuple in choice_tuples:
                if choice_tuple[2] is not None:
                    import_line = self._get_import_from_ref(choice_tuple[2])
                    if import_line not in import_lines:
                        self._write(2, import_line)
                        import_lines.append(import_line)
            choices = []
            for choice_tuple in choice_tuples:
                choices.append(choice_tuple[0])
            self._write(2, 'if isinstance(choice, (%s)) is False:' % (', '.join(choices)))
            self._write(3, "raise TypeError('choice must be of type: %s')" % (', '.join(choices)))
            self._write(2, "self.__setattr__('choice', %s._CHOICE_MAP[type(choice).__name__])" % classname)
            self._write(2, "self.__setattr__(%s._CHOICE_MAP[type(choice).__name__], choice)" % classname)
        else:
            for name, property in schema['properties'].items():
                if '$ref' in property:
                    import_line = self._get_import_from_ref(property['$ref'])
                    if import_line not in import_lines:
                        self._write(2, import_line)
                        import_lines.append(import_line)
            for name, property in schema['properties'].items():
                restriction = self._get_isinstance_restriction(property)
                self._write(2, 'if isinstance(%s, %s) is True:' % (name, restriction))
                self._write(3, 'self.%s = %s' % (name, name))
                self._write(2, 'else:')
                self._write(3, "raise TypeError('%s must be an instance of %s')" % (name, restriction))

    def _get_isinstance_restriction(self, property):
        if '$ref' in property:
            return '(%s, type(None))' % self._get_classname_from_ref(property['$ref'])
        elif property['type'] in ['number', 'integer']:
            return '(float, int, type(None))'
        elif property['type'] == 'string':
            return '(str, type(None))'
        elif property['type'] == 'array':
            return '(list, type(None))'

    def _get_type_restriction(self, property):
        if '$ref' in property:
            ref_obj = self._get_object_from_ref(property['$ref'])
            if 'description' in ref_obj:
                property['description'] = ref_obj['description']
            return 'Union[%s, type(None)]' % self._get_classname_from_ref(property['$ref'])
        elif property['type'] in ['number', 'integer']:
            return 'Union[float, int, type(None)]'
        elif property['type'] == 'string':
            return 'Union[str, type(None)]'
        elif property['type'] == 'array':
            return 'Union[list[%s], type(None)]' % self._get_type_restriction(property['items'])

    def _get_object_from_ref(self, ref):
        from jsonpath_ng import jsonpath, parse
        pieces = ref.split('/')
        json_path = '$.%s."%s"' % ('.'.join(pieces[1:-1]), pieces[-1])
        return parse(json_path).find(self._openapi)[0].value

    def _get_import_from_ref(self, ref):
        filename = '_'.join(ref.lower().split('#/components/schemas/')[-1].split('.')[0:-1])
        classname = self._get_classname_from_ref(ref)
        return 'from abstract_open_traffic_generator.%s import %s' % (filename, classname)

    def _get_classname_from_ref(self, ref):
        final_piece = ref.split('/')[-1]
        if '.' in final_piece:
            return final_piece.split('.')[-1]
        else:
            return final_piece

    def _write(self, indent=0, line=''):
        self._fid.write('    ' * indent + line + '\n')

    def _bundle(self, base_dir, api_filename, output_filename):
        print('bundling started')
        self._read_file(base_dir, api_filename)
        with open(self._output_filename, 'w') as fid:
            yaml.dump(self._content, fid, indent=2, sort_keys=False)
        print('bundling complete')

    def _read_file(self, base_dir, filename):
        filename = os.path.join(base_dir, filename)
        filename = os.path.abspath(os.path.normpath(filename))
        base_dir = os.path.dirname(filename)
        with open(filename) as fid:
            yobject = yaml.safe_load(fid)
        self._process_yaml_object(base_dir, yobject)

    def _process_yaml_object(self, base_dir, yobject):
        for key, value in yobject.items():
            if key in ['openapi', 'info', 'servers'] and key not in self._content.keys():
                self._content[key] = value
            elif key in ['paths']:
                if key not in self._content.keys():
                    self._content[key] = {}
                for sub_key in value.keys():
                    self._content[key][sub_key] = value[sub_key] 
            elif key == 'components':
                if key not in self._content.keys():
                    self._content[key] = {
                        'schemas': {}
                    }
                if 'schemas' in value:
                    schemas = value['schemas']
                    for schema_key in schemas.keys():
                        self._content['components']['schemas'][schema_key] = schemas[schema_key]
        self._resolve_refs(base_dir, yobject)

    def _resolve_refs(self, base_dir, yobject):
        """Resolving references is relative to the current file location
        """
        if isinstance(yobject, dict):
            for key, value in yobject.items():
                if key == '$ref' and value.startswith('#') is False:
                    refs = value.split('#')
                    print('resolving %s' % value)
                    self._read_file(base_dir, refs[0])
                    yobject[key] = '#%s' % refs[1]
                elif isinstance(value, str) and 'x-inline' in value:
                    refs = value.split('#')
                    print('inlining %s' % value)
                    inline = self._get_inline_ref(base_dir, refs[0], refs[1])
                    yobject[key] = inline
                else:
                    self._resolve_refs(base_dir, value)
        elif isinstance(yobject, list):
            for item in yobject:
                self._resolve_refs(base_dir, item) 

    def _get_inline_ref(self, base_dir, filename, inline_key):
        filename = os.path.join(base_dir, filename)
        filename = os.path.abspath(os.path.normpath(filename))
        base_dir = os.path.dirname(filename)
        with open(filename) as fid:
            yobject = yaml.safe_load(fid)
        return parse('$%s' % inline_key.replace('/', '.'), ).find(yobject)[0].value
                        

if __name__ == '__main__':
    builder = Builder(dependencies=True, clone_and_build=True)

    import yaml

    builder.generate()

