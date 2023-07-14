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

    def get_avg(self):
        print(self.marks)
        avg = sum(self.marks)/len(self.marks)
        print(avg)

    
s1 = Student('ahmed')
s2 = Student('Ali')

s1.add_mark(50)
s2.add_mark(40)
s1.add_mark(30)
s1.add_mark(80)
s2.add_mark(90)
s1.add_mark(40)
s2.add_mark(20)
s2.add_mark(80)


s1.get_avg()
s2.get_avg()
