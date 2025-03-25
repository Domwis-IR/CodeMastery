from collections import deque
def order_student(students, student_num):
    extra_line = []

    students = deque(students)
    n = 1

    while students or extra_line:
        if not students and n != extra_line[-1]:
            break

        if students and students[0] == n:
            student = students.popleft()
            n += 1
        elif extra_line and n == extra_line[-1]:
            student = extra_line.pop()
            n += 1
        else:
            student = students.popleft()
            extra_line.append(student)
    
    # print("extra_line", extra_line)
    # print("received", received)

    return "Nice" if not extra_line else "Sad"


def __main__():
    student_num = int(input())
    students = list(map(int, input().split()))
    answer = order_student(students, student_num)
    print(answer)

if __name__ == "__main__" :
    __main__()