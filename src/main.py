import argparse
import curses
import cli


def main(args):
    pass


if __name__ == '__main__':

    menu = cli.CLIMenu('Select your favourite languages', ['Java', 'Python', 'C++'], True)
    print(menu.open())

    # parser = argparse.ArgumentParser()
    #
    # # General commands
    # parser.add_argument('init', help='Generate build_scheme.json')
    # parser.add_argument('run', help='Start docker containers')
    # parser.add_argument('stop', help='Stop docker containers and remove one')
    # parser.add_argument('build', help='Generate nginx image, build git images, generate docker-compose.yml')
    #
    # # Units manager
    # parser.add_argument('add', metavar='template', nargs=1, type=str, help='Generate from template or add scheme')
    # parser.add_argument('rm')
    # parser.add_argument('list')
    #
    # args = parser.parse_args()
    # main(args)
