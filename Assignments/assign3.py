#import datetime

class Student:
    def __init__(self, roll_number, name, dob, address):
        self.roll_number = roll_number
        self.name = name
        self.dob = dob
        self.address = address

    def __str__(self):
        return f"Roll Number: {self.roll_number}, Name: {self.name}, Date_Of_Birth: {self.dob}, Address: {self.address}"


class SchoolManagementSystem:
    def __init__(self):
        self.students_dict = {}

    def add_student(self, student):
        if student.roll_number not in self.students_dict:
            self.students_dict[student.roll_number] = student
            print(f"Student with Roll Number {student.roll_number} added successfully.")
        else:
            raise ValueError(f"Student with Roll Number {student.roll_number} already exists.")

    def update_student(self, roll_number, updated_student):
        if roll_number in self.students_dict:
            self.students_dict[roll_number] = updated_student
            print(f"Student with Roll Number {roll_number} updated successfully.")
        else:
            raise ValueError(f"Student with Roll Number {roll_number} not found.")

    def delete_student(self, roll_number):
        if roll_number in self.students_dict:
            del self.students_dict[roll_number]
            print(f"Student with Roll Number {roll_number} deleted successfully.")
        else:
            raise ValueError(f"Student with Roll Number {roll_number} not found.")

    def display_students(self):
        print("List of Students:")
        for roll_number, student in self.students_dict.items():
            print(student)

# Main program

def main():
    school_system = SchoolManagementSystem()

    while True:
        print("\nSchool Management System Menu:")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                roll_number = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                dob = int(input("Enter Date of Birth: "))
                
               # date_entry = input('Enter a date in YYYY-MM-DD format')
                #year, month, day = map(int, date_entry.split('-'))
                #dob = datetime.date(year, month, day)

                address = input("Enter Address: ")
                new_student = Student(roll_number, name, dob, address)
                school_system.add_student(new_student)

            elif choice == 2:
                roll_number = int(input("Enter Roll Number of the student to update: "))
                name = input("Enter Updated Name: ")
                dob = int(input("Enter Updated Date of Birth: "))
                address = input("Enter Updated Address: ")
                updated_student = Student(roll_number, name, dob, address)
                school_system.update_student(roll_number, updated_student)

            elif choice == 3:
                roll_number = int(input("Enter Roll Number of the student to delete: "))
                school_system.delete_student(roll_number)

            elif choice == 4:
                school_system.display_students()

            elif choice == 5:
                print("Exiting School Management System.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        except ValueError as e:
            print(f"Error: {e}. Please enter valid input.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
            
            
            
if __name__=="__main__":
    print("Welcome to School management System")
    main()
        
        
        
