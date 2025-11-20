import sys
#check if correct number of arguments 
if len(sys.argv) != 3:
    print("Usage :python student.py <name> <rollno>")
    sys.exit(1)
script_name = sys.argv[0]
name = sys.argv[1]
rollno = sys.argv[2]
print("script Name:",script_name)
print("script Name:",name)
print("Roll Number:",rollno)
