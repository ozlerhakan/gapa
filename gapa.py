import rumps
import os

from subprocess import call

FILE_NAME_STATUS = "gapak"


class Gapa(rumps.App):

    def __init__(self, name):
        super().__init__(name, icon='images/circle.png', menu=['Toggle Desktop Items', None, 'Quit'], quit_button=None)
        try:
            with open(FILE_NAME_STATUS, "r") as file:
                self.__isHidden = (file.readlines().pop(0) == 'True')
        except FileNotFoundError:
            self.__isHidden = False

    @rumps.clicked('Toggle Desktop Items')
    def hide(self, _):
        desktop = '{0}/Desktop/**'.format(os.path.expanduser('~'))
        if not self.__isHidden:
            call("/usr/bin/chflags hidden " + desktop, shell=True)
            self.__isHidden = True
        else:
            call("/usr/bin/chflags nohidden " + desktop, shell=True)
            self.__isHidden = False

    @rumps.clicked('Quit')
    def clean_up_before_quit(self, _):
        with open(FILE_NAME_STATUS, "w") as file:
            file.write(str(self.__isHidden))
        rumps.quit_application()


if __name__ == "__main__":
    app = Gapa("gapa")
    app.run()
