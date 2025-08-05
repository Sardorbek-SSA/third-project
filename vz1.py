class Student:
    def __init__(self,first_name,last_name,age,student_id,course):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = None
        self.age = age
        self.__student_id = student_id
        self.__course = course
        self.course = course
        
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def age(self):
        return self.__age
    
    @property
    def student_id(self):
        return self.__student_id
    
    @property
    def course(self):
        return self.__course
    
    @first_name.setter
    def first_name(self,firstname):
        self.__first_name = firstname
        
    @last_name.setter
    def last_name(self,lastname):
        self.__last_name = lastname
        
    @age.setter
    def age(self,age):
        if 18 <= age <= 30:
            self.__age = age
        else:
            print("Yosh 18 dan 30 gacha bo'lishi kerak")
            
    @course.setter
    def course(self,course):
        if 1 <= course <= 4:
            self.__course = course
        else:
            print("Kurs 1dan 4gacha")
            
    def increase_course(self):
        if self.__course < 4:
            self.__course +=1
        else:
            print("Kurs maksimal 4ga yetgan")
            
    def update_student_id(self,new_id,username,password):
        if username == self.__first_name and password == "1234":
            self.__student_id = new_id
            print("Talaba raqami yangilandi")
        else:
            print("Foydalanuvchi nomi yoki parol xato")
            
first_name = input("Talabaning ismi: ")
last_name = input("Familya: ")

while True:
    try:
        age = int(input("Yoshi(18-30): "))
        if 18 <= age <= 30:
            break
        else:
            print("Yosh 18dan 30gacha. Qayta kiriting: ")
    except ValueError:
        print("Iltimos to'g'ri raqam kiriting: ")

student_id = input("Talaba raqami: ")

while True:
    try:
        course = int(input("Talabaning kursi(1-4): "))
        if 1 <= course <= 4:
            break
        else:
            print("Kurs 1dan 4gacha. Qayta kiriting: ")
    except ValueError:
        print("Iltimos to'g'ri raqam kiriting: ")
        
talaba = Student(first_name,last_name,age,student_id,course)

print("\n--- Talaba ma'lumotlari ---")
print("Ism: ",talaba.first_name)
print("Familya: ",talaba.last_name)
print("Yosh: ",talaba.age)
print("Talaba raqami: ",talaba.student_id)
print("Kurs: ",talaba.course)

talaba.increase_course()
print("Kurs oshirildi: ",talaba.course)

print("\nTalaba raqamini yangilash uchun login va parol kiriting")
username = input("Username(Ism): ")
password = input("Parol: ")
new_id = input("Yangi talaba raqami: ")

talaba.update_student_id(new_id,username,password)
print("Hozirgi talaba raqami: ",talaba.student_id)