class Teacher :
    def __init__(self, id, branch, name, surname, birth_date, gender) :
        if id is None :
            self.id = 0
        else :
            self.id = id
        self.branch = branch
        self.name = name
        self.surname = surname
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender