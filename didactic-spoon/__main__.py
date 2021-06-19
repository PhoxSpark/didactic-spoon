"""
"""
import argparse
import logging
import tkinter
import os
from .src import todo

def start():
    """
    Initialize the application and start the propper functions.
    """
    args = parse_arguments()
    log = initialize_logger()

    log.debug("Arguments parsed and logging initialized, calling main function...")
    todo.start(args, log)

def parse_arguments():
    """
    Initialize argparse and collects arguments.
    Standard among codes.
    """
    parser = argparse.ArgumentParser(description="To-Do list with GUI (and CLI).")

    return parser

def initialize_logger():
    """
    Initialize logger.
    Standard among codes.
    """

    logger = None       # Store the logger object and makes logs.
    fh = None           # File handler.
    ch = None           # Console handler.
    formatter = None    # Format of the output.

    try:
        os.remove("debug.log")
    except:
        pass
    
    logger = logging.getLogger("logger")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("debug.log")
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)
    print(type(logger))
    return logger

def tk_test():
    """
    Just to test the tkinter library.
    """
    root=tkinter.Tk()
    a = tkinter.Label(root, text="Hello, world!")
    a.pack()
    root.mainloop()

if __name__ == "__main__":
    start()
