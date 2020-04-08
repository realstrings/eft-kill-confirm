from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tempfile
from playsound import playsound
print('''
                                                                            
,--. ,--.,--.,--.,--.     ,-----.                ,---.,--.                  
|  .'   /`--'|  ||  |    '  .--./ ,---. ,--,--, /  .-'`--',--.--.,--,--,--. 
|  .   ' ,--.|  ||  |    |  |    | .-. ||      \|  `-,,--.|  .--'|        | 
|  |\   \|  ||  ||  |    '  '--'\' '-' '|  ||  ||  .-'|  ||  |   |  |  |  | 
`--' '--'`--'`--'`--'     `-----' `---' `--''--'`--'  `--'`--'   `--`--`--' 
                                                                            
                                                                 by Strings
Visit quality.gg for cheap Netflix etc...
You can now Minimize me.
''')

tempdir=tempfile.gettempdir()
class Watcher:
    DIRECTORY_TO_WATCH = tempdir+"\Highlights\Escape From Tarkov"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                pass
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.event_type == 'created':
            playsound('sound.mp3')
        else:
            pass


if __name__ == '__main__':
    w = Watcher()
    w.run()