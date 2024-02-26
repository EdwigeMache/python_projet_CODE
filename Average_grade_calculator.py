

student_note1= float(input("enter student's in physics : "))
student_note2= float(input("enter student's in compter science : "))
student_note3= float(input("enter student's in chemistry : "))
student_note4= float(input("enter student's in english : "))
student_note5= float(input("enter student's in french : "))

average =0.2* (student_note1+student_note2+student_note3+student_note4+student_note5)

if average>=0 and average<=100:

  if student_note1>90:
    print("Average", average, "grade: A") 
  elif student_note2>80:
    print("Average", average, "grade: B") 
  elif student_note3>70:
     print("Average", average, "grade: C") 
  elif student_note4>60:
    print("Average", average, "grade: D") 
  else:
    print("FAILED")