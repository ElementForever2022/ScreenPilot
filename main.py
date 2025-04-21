import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

# Create a basic window class
class ExampleMyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set window properties
        self.setWindowTitle("Simple Qt Demo") # Title of the window(on the toolbar)
        self.setGeometry(100, 1000, 300, 200) # position of window at startup(leftup-xy, rightbottom-xy)

        # Create a button
        button = QPushButton("Click Me!", self)
        button.setGeometry(100, 80, 100, 40)
        button.clicked.connect(self.show_message)

    def show_message(self):
        QMessageBox.information(self, "Message", "Hello from PyQt5!")

class BaseWindow(QWidget):
    def __init__(
            self, 
            window_name:str|None=None, # name of the window on toolbar
            window_position_startup:tuple|None=None, # position of window's left-up corner at startup(x,y), where x is right(→) and y is down(↓)
            window_size:tuple|None=None # width and height of the window
        ):
        """
        params:
            `window_name`:str|None=None,                  # name of the window on toolbar
            `window_position_startup`:tuple|None=None,    # position of window's left-up corner at startup(x,y), where x is right(→) and y is down(↓)
            `window_size`:tuple|None=None                 # width and height of the window
        """
        super().__init__()
        
        # Dealing with possible exceptions
        # Type Errors
        if window_name==None:
            raise Exception('Must provide a window name!')
        if window_position_startup==None:
            raise Exception('Must provide the initial position of the window!')
        if window_size==None:
            raise Exception('Must provide size of the window')
        # Num of Param Error
        if len(window_position_startup)!=2:
            raise Exception(f'Size of tuple of "window_position_startup" at startup error, 2 wanted, {len(window_position_startup)} given')
        if len(window_size)!=2:
            raise Exception(f'Size of tuple of "window_size" at startup error, 2 wanted, {len(window_size)} given')
        
        # register the data members
        self.window_name = window_name # name of the window on toolbar
        self.window_position_startup = window_position_startup # position of window's left-up corner at startup(x,y), where x is right(→) and y is down(↓)
        self.window_size = window_size # height and width of the window
        
        # initialize the gui(bottons and images EXcluded)
        self.init_window()
    
    def init_window(self):
        """
        applying all the INITIAL components to the gui
        including window_name, window_position_startup, window_size
        nothing else, bottons and images excluded.
        """
        # set up the title of the window
        self.setWindowTitle(self.window_name)
        
        # set the window frame geometry
        left_up_x = self.window_position_startup[0]
        left_up_y = self.window_position_startup[1]
        window_width = self.window_size[0]
        window_height = self.window_size[1]
        self.setGeometry(left_up_x, left_up_y, window_width, window_height)
    
        
class AppWindow(BaseWindow):
    def __init__(self, 
            app: QApplication,
            window_name = "Screen Pilot",
            window_width = 700,
            window_height = 500
        ):
        # get the size of the WHOLE screen
        screen = app.primaryScreen()
        screen_size = screen.size()
        MAIN_SCREEN_WIDTH, MAIN_SCREEN_HEIGHT = (screen_size.width(), screen_size.height())
        
        # calculate the position of the window
        left_up_x = MAIN_SCREEN_WIDTH//2-window_width//2
        left_up_y = MAIN_SCREEN_HEIGHT//2-window_height//2
        # initialize
        super().__init__(
            window_name,
            (left_up_x, left_up_y),
            (window_width, window_height)
        )


def main():
    # app = QApplication(sys.argv)
    # window = BaseWindow(
    #     'window',
    #     (200,200),
    #     (200,200)
    # )
    # window.show()
    # sys.exit(app.exec_())
    
    # app = QApplication([])
    # screen = app.primaryScreen()
    # size = screen.size()
    # print(size)
    
    app = QApplication(sys.argv)
    window_app = AppWindow(app)
    window_app.show()
    sys.exit(app.exec_())
    
    


# Run the application
if __name__ == "__main__":
    main()