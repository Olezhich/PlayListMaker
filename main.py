import python.app
import sys

def main():
    if len(sys.argv) < 2:
        print(f'{sys.argv[0]}: no args')
        return

    application = python.app.App()

    for arg in sys.argv[1:]:
        if arg == 'make':
            application.make_plst()

        if arg == 'update':
            application.update_current()

        if arg == 'last':
            print(application.get_last())

        if arg == 'get':
            application.get_plst()

        if arg == 'help':
            print('options:')
            print('[make, update, last, get]')


if __name__ == "__main__":
    main()



