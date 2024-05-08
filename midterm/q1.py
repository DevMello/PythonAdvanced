def get_grades():
    while True:
        grades_input = input("Enter a set of numeric grades (separated by commas): ")
        if grades_input == "":
            print("Exiting...")
            return []
        try:
            grades = [int(grade.strip()) for grade in grades_input.split(",")]
            return grades
        except ValueError:
            print("Entry error. Please enter numeric grades only.")

def print_sorted_grades(grades):
    n = len(grades)
    for i in range(n):
        for j in range(0, n-i-1):
            if grades[j] > grades[j+1] :
                grades[j], grades[j+1] = grades[j+1], grades[j]
    print("Sorted grades:", grades)

def get_highest_grade(grades):
    highest_grade = grades[0]
    for grade in grades:
        if grade > highest_grade:
            highest_grade = grade
    return highest_grade

def get_average_grade(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

def get_lowest_grade(grades):
    lowest_grade = grades[0]
    for grade in grades:
        if grade < lowest_grade:
            lowest_grade = grade
    return lowest_grade


while True:
    grades = get_grades()
    if not grades:
        break

    print_sorted_grades(grades)
    highest_grade = get_highest_grade(grades)
    average_grade = get_average_grade(grades)
    lowest_grade = get_lowest_grade(grades)

    print("Highest grade:", highest_grade)
    print("Average grade:", average_grade)
    print("Lowest grade:", lowest_grade)