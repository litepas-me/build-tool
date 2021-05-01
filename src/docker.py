import yaml
from obj import Service
from scheme import Scheme


def generate_compose_file(scheme: Scheme):
    compose_yaml = dict()
    compose_yaml['version'] = scheme.version

    services = dict()
    for service in scheme.services:
        service_yaml = dict()

        service_yaml['image'] = service.image
        service_yaml['restart'] = 'always'
        service_yaml['ports'] = service.ports

        services[service.name] = service_yaml
