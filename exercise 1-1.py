'''
student:

    - creat student (name) -> welcome
    - add mark
    - get avg

'''

class Student:
    def __init__(self,name):
        print (f'Welcome {name}')
        #self.name = name
        self.marks = []

    def add_mark(self,mark):
        self.marks.append(mark)

    
s1 = Student('ahmed')

s1.add_mark(50)

