from unicodedata import name


class Person():
    
    def __init__(self,  name, surname): 
        self.name = name
        self.surname = surname
   

    @property
    def fullname(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    @fullname.setter
    def fullname(self, new_full_name):
        space_index = new_full_name.index(' ')
        self.name = new_full_name[:space_index]
        self.surname = new_full_name[space_index+1:]
        return new_full_name

    def get_name(self):
        print(self.name)

    # def get_full_name(self):
    #     print(self.full_name)


p1 = Person('Murad', 'Aliyev', )
p1.get_name()
p1.name = 'Turan'
p1.get_name()
p1.fullname = 'Ali Aliyev'
print(p1.fullname)
p1.get_name()


# p2.get_name()