from Executive import Executive
#main, takes file name and starts executive function
def main(self):
    try:
        file_name = input('Enter file name: ')
    except:
        RuntimeError("File not found")
    my_executive = Executive()
    my_executive.executive(file_name)

main(None)