
class Service:
    name: str
    image: str
    ports: dict
    properties: dict
    nginx_conf: str

    def __init__(self, name: str, image: str, ports: dict, properties: dict, nginx_conf: str) -> None:
        super().__init__()
        self.name = name
        self.image = image
        self.ports = ports
        self.properties = properties
        self.nginx_conf = nginx_conf
