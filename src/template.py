import json
from enum import Enum
from os import path


TEMPLATES_DIR = './templates/'


class RequireType(Enum):
    STRING = 'str'
    INTEGER = 'int'
    BOOLEAN = 'bool'
    ENUM = 'enum'

    @staticmethod
    def from_name(name: str):
        if name == RequireType.STRING.value:
            return RequireType.STRING
        elif name == RequireType.INTEGER.value:
            return RequireType.INTEGER
        elif name == RequireType.BOOLEAN.value:
            return RequireType.BOOLEAN
        elif name == RequireType.ENUM.value:
            return RequireType.ENUM
        else:
            raise TypeError


class Require:
    name: str           # Require
    type_: RequireType  # Require
    min_: int           # Optional | Only if type is integer
    max_: int           # Optional | Only if type is integer
    chooses: list[str]  # Require | Only if type is enum
    is_multiple: bool   # Optional | Only if type isn't boolean

    def __init__(self, name: str, type_: RequireType, min_: [int, None], max_: [int, None], chooses: [list[str], None]) -> None:
        self.name = name
        self.type_ = type_
        self.min_ = min_
        self.max_ = max_
        self.chooses = chooses


class Template:
    name: str
    author: str
    version: str
    file: str
    requires: list[Require]

    def __init__(self, name: str, author: str, version: str, file: str, requires: list[Require]) -> None:
        self.name = name
        self.author = author
        self.version = version
        self.file = file
        self.requires = requires


def __get_if_exists__(json_, key):
    if key in json_:
        return json_[key]

    return None


def read_template(name: str):
    template_manifest_file_path = f'{TEMPLATES_DIR}{name}/manifest.json'
    template_file_path = f'{TEMPLATES_DIR}{name}/template.txt'

    if not path.exists(template_manifest_file_path) or not path.isfile(template_manifest_file_path):
        raise FileNotFoundError(f'{template_manifest_file_path} not found')

    if not path.exists(template_file_path) or not path.isfile(template_file_path):
        raise FileNotFoundError(f'{template_file_path} not found')

    template_manifest_file = open(template_manifest_file_path, 'r')
    manifest_json = json.load(template_manifest_file)
    template_manifest_file.close()

    template_file = open(template_file_path)
    template_txt = template_file.read()
    template_file.close()

    author = manifest_json['author']
    version = manifest_json['version']
    file = template_txt

    requires = list[Require]()

    for require_json in manifest_json[requires]:
        name = require_json['name']
        type_ = RequireType.from_name(require_json['type'])

        if type_ == RequireType.INTEGER:
            min_ = __get_if_exists__(require_json, 'min')
            max_ = __get_if_exists__(require_json, 'max')

            requires.append(Require(name, type_, min_, max_, None))
            continue

        if type_ == RequireType.ENUM:
            chooses = require_json['chooses']

            requires.append(Require(name, type_, None, None, chooses))
            continue

        requires.append(Require(name, type_, None, None, None))

    return Template(name, author, version, file, requires)


def generate_service(template: Template):
    print(f'''
    Using {template.name} {template.version}
    Created by {template.author}
    ''')

    for require in template.requires:
        pass


