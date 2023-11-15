

def input_with_validation(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            number = int(user_input)
            if 1 <= number <= 100:
                return number
            else:
                print("Please enter a number between 1 and 100.")
        else:
            print("Please enter a valid number.")


subjects = ['bangla', 'english', 'math', 'science']
marks = []
total = 0


for subject in subjects:
    sub_marks = input_with_validation(f'Enter the marks in {subject} : ')
    marks.append(sub_marks)

# print(marks)
# print(type(marks[0]))

for mark in marks:
    total += mark

# print(total)

average = total / len(subjects)
print(average)

if average <= 40:
    grade = 'F';
elif average <= 60:
    grade = 'D'
elif average <= 70:
    grade = 'C'
elif average <= 80:
    grade = 'B'
elif average <= 90:
    grade = 'A'
elif average <= 100:
    grade = 'A+'
else:
    grade = 'Not available'

print(grade)


print(
'''---------------------------------------
        R   E   S   U   L   T        
---------------------------------------'''
)

print('individual Marks:')
for i in range(0, len(subjects)):
    print(f'{subjects[i]} : {marks[i]}')

print(f'\nAverage Marks: {average}' )

print(f'\nFinal Grade: {grade}')



