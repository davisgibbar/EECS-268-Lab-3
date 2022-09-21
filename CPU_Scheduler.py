from Queue_file import queue_class
from Stack_file import stack_class

#takes info from executive, creates stack, pushes on main
class cpu_scheduler:
    def __init__(self, processName):
        self.processName = processName
        self.stack = stack_class()
        self.stack.push("main")