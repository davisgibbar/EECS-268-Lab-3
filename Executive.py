from CPU_Scheduler import cpu_scheduler
from Queue_file import queue_class

#takes in file name, reads through file, creates a 2d list and
#reads the first input of each value of the list which then
#does necessary actions per command
class Executive:
    def __init__(self):
        self.mainQueue= queue_class()

    def executive(self, file_name):
        str(file_name)
        input_file = open(file_name)
        list_commands = []
        for count, line in enumerate(input_file.readlines()):
            each_word = []
            for index, word in enumerate(line.split(" ")):
                each_word.append(word.rstrip("\n"))
            list_commands.append(each_word)

        for eachLine in list_commands:
            #takes start command, queues on process name and prints the action done
            if eachLine[0] == 'START':
                self.mainQueue.enqueue(cpu_scheduler(eachLine[1]))
                print(eachLine[1] + ' is added to the queue')
            #takes call command, pushes function name onto stack, prints action done, and moves process name to back of queue
            elif eachLine[0] == "CALL":
                self.mainQueue.peek_front().stack.push(eachLine[1])
                print(self.mainQueue.peek_front().processName + ' calls '+ eachLine[1])
                self.mainQueue.enqueue(self.mainQueue.dequeue())
            #takes command return and if the value at top of stack is main
            #returns the process and ends process. If main is not at top of stack
            #pops value on top of stack, prints process returns from funtion,
            #and moves value at front of queue to the back
            elif eachLine[0] == "RETURN":
                if self.mainQueue.peek_front().stack.peek() == 'main':
                    print(self.mainQueue.peek_front().processName + ' returns from main')
                    print(self.mainQueue.peek_front().processName + ' process has ended')
                    self.mainQueue.dequeue()
                else:
                    fName = self.mainQueue.peek_front().stack.pop()
                    print(self.mainQueue.peek_front().processName + ' returns from '+fName)
                    self.mainQueue.enqueue(self.mainQueue.dequeue())
            else:
                RuntimeError("Command not found")