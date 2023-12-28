import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os


class MyHandler(FileSystemEventHandler):
    def __init__(self, main_file, dependencies):
        super().__init__()
        self.main_file = main_file
        self.dependencies = dependencies  # Add your dependencies here

    def on_modified(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".py") and not event.src_path.endswith("watcher.py"):
            print(f"Detected change in {event.src_path}")
            subprocess.run(["python", self.main_file], shell=True)
            if self.main_file in event.src_path or any(
                dep in event.src_path for dep in self.dependencies
            ):
                print("Detected change in main.py or its dependencies.")
                subprocess.run(["python", self.main_file], shell=True)


if __name__ == "__main__":
    # main file name
    main_file = "src/main.py"

    # and it's dependencies
    watched_dependencies = [
        "Bot.py",
        "static.py",
        "access.py",
        "Json.py",
    ]

    event_handler = MyHandler(main_file, watched_dependencies)
    observer = Observer()

    PATH = "."  # default path is the current folder

    observer.schedule(event_handler, PATH, recursive=True)
    observer.start()

    print(f"I'm watching the {PATH} folder. Now go and do your job")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
