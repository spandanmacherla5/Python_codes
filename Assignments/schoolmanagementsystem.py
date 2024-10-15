class Student:
    def __init__(self,name,dob,address,standard):
        self.stu_name=name
        self.stu_dob=dob
        self.address=address 
        self.standard=standard
        
        
class SchoolManagementSyatem:
    def __init__(self):
        self.stu_dict={}
        
    def add_new_student(self,student):
        if student.id not in self.stu_dict:
            self.stu_dict[student.id] = student
            print(f"Student with Roll Number {student.id} added successfully.")
        else:
            raise ValueError(f"Student with Roll Number {student.id} already exists.")

        
   
   
def main():
    school_system=SchoolManagementSyatem()     
    
    try:
        choose = int(input("Enter the choice of operation you want to do\n############################################# \n1.Add \n2.Update \n3.Delete \n4.SeeAll \n"))
        
        if choose in (1,2,3,4):
            
            if choose == 1:
                id = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                dob = input("Enter DOB: ")
                address = input("Enter address: ")
                standard = input("Enter standard: ")
                new_student = Student(id, name, dob, address,standard)
                school_system.add_new_student(new_student)
                
                
    
    
    except ValueError as ex:
        print(f"Error: {ex}. Please enter valid input.")

                
        
if __name__=="__main__":
    print("Welcome to School management System")
    main()
        
    
    