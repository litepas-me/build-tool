from obj import Service


class Scheme:
    name: str
    version: str
    author: str
    git: str
    services: list[Service]

    def __init__(self, name: str, version: str, author: str, git: str, services: list[Service]) -> None:
        self.name = name
        self.version = version
        self.author = author
        self.git = git
        self.services = services


def save_scheme(scheme: Scheme) -> dict:
    scheme_json = dict()
    scheme_json['name'] = scheme.name
    scheme_json['version'] = scheme.version
    scheme_json['author'] = scheme.author
    scheme_json['git'] = scheme.git

    services_json = list()

    for service in scheme.services:
        service_json = dict()
        service_json['name'] = service.name
        service_json['image'] = service.image
        service_json['ports'] = service.ports
        service_json['properties'] = service.properties
        service_json['nginx-conf'] = service.nginx_conf

        services_json.append(service_json)

    return scheme_json


def load_scheme(json: dict) -> Scheme:
    name = json['name']
    version = json['version']
    author = json['author']
    git = json['git']

    services = list()

    for service_json in json['services']:
        service_name = service_json['name']
        service_image = service_json['image']
        service_ports = service_json['ports']
        service_properties = service_json['properties']
        service_nginx_conf = service_json['nginx-conf']

        services.append(Service(service_name, service_image, service_ports, service_properties, service_nginx_conf))

    return Scheme(name, version, author, git, services)
