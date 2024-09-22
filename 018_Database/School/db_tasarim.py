## veritabanı tasarımı

# ALTER TABLE class
# ADD CONSTRAINT fk_teacher_class
# FOREIGN KEY (teacherid) REFERENCES teacher(id)

# ALTER TABLE student
# ADD CONSTRAINT fk_student_class
# FOREIGN KEY (classid) REFERENCES class(id)

# ALTER TABLE class_lesson
# ADD CONSTRAINT fk_class_lesson_class
# FOREIGN KEY (classid) REFERENCES class(id);

# ALTER TABLE class_lesson
# ADD CONSTRAINT fk_class_lesson_lesson
# FOREIGN KEY (lessonid) REFERENCES lesson(id);

# ALTER TABLE class_lesson
# ADD CONSTRAINT fk_class_lesson_teacher
# FOREIGN KEY (teacherid) REFERENCES teacher(id)

'''

student
---------------------
id
student_number
name
surname
birthdate
gender
classid


teacher
---------------------
id
branch
name
surname
birthdate
gender


class
---------------------
id
name
teacherid


lesson
---------------------
id
name



class_lesson
---------------------
classid
lessonid
teacherid





'''