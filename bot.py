from controller import Controller


def main():
    controller = Controller()
    # FIXME: exception catcher at process level
    while True:
        controller.process()


main()
