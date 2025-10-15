#first_name="Dilafruz"
#last_name="Ongarbaeva"
#student_id= 20071205
#gpa=3.85
#is_schoolarship_eligible= True

#print(f"Student: {first_name} {last_name}")
#print(f"ID: {student_id}")
#print(f"GPA: {gpa}")
#print(f"Schoolarship: {'Yes' if is_schoolarship_eligible ==True else 'No'}")

#name = "Dilafruz"
#message = 'Good morning!'
#address = "123 Main Street, Urgench"
#print(type(name))
#print(type(message))
#print(type(address))

#a = 9
#b = 2
#sum_result = a+b
#print(f"{a} + {b} = {sum_result}")
#difference = a - b
#print(f"{a} - {b} = {difference}")
#product = a * b
#print(f"{a} * {b} = {product}")
#quotient = a / b
#print(f"{a} / {b} = {quotient}")
#floor_div = a // b
#print(f"{a} // {b} = {floor_div}")
#remainder = a % b
#print(f"{a} % {b} = {remainder}")
#power = a ** b
#print(f"{a} ** {b} = {power}")

#length = 7
#width = 4.5
#area = length * width
#perimeter = 2 * (length + width)

#print(f"Rectangle dimensions: {length}m x {width}m")
#print(f"Area: {area} square meters")
#print(f"Perimeter: {perimeter} meters")

#celsius=float(input("enter celsius: "))
#in_Fahrenheit=(celsius * 9/5) + 32
#in_Kelvin= celsius + 273.15
#print(f"Fahrenheit: {in_Fahrenheit}")
#print(f"Kelvin: {in_Kelvin}")

#r=float(input("Please enter temperaure: "))
#pi=3.14159
#area=pi*r**2
#circumference=2*pi*r
#print(f"Area: {area: .2f}\nCircumference: {circumference: .2f}")

student_name=input("enter your name: ")
gpa=float(input("enter your GPA: "))
credits=int(input("enter your total credit hours: "))
deans_list=({gpa},{credits})
student_information=(f"Student name: {student_name}\nGPA: {gpa}\nCredit hours: {credits}")
print(bool(deans_list))
print(student_information)
print(f"Deans list: {"True" if deans_list else "False"}")
print(f"How many more GPA points needed: {"no need" if gpa>=3.5 else 3.5-gpa}")
print(f"How many more credits needed: {"no need" if credits>=12 else 12-credits}")
