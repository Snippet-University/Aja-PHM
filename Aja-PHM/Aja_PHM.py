import wpf

from System.Windows import Application, Window

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'Aja_PHM.xaml')
    

if __name__ == '__main__':
    Application().Run(MyWindow())
