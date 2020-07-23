from pywinauto.application import Application
from all_function import *


def main():
    keda = '"C:\\Program Files (x86)\\Bourevestnik\\KEDA\\kedaw.exe" -sim -spec=sim   -hvpsvst=0.2 --devdetflt=bra-135  --measerrordlg'
    app = Application().start(keda)
    print(login(app))


if __name__ == '__main__':
    main()
