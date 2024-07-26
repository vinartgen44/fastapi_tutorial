from datetime import date

from models.student import Student


student_data = {
    "student_id": 1,
    "phone_number": "+1234567890",
    "first_name": "Иван",
    "last_name": "Иванов",
    "date_of_birth": date(2000, 1, 1),
    "email": "ivan.ivanov@example.com",
    "address": "Москва, ул. Пушкина, д. Колотушкина",
    "enrollment_year": 2012,
    "major": "Информатика",
    "course": 3,
    "special_notes": "Увлекается программированием"
}

def test_validate_student() -> None:
    try:
        student = Student(**student_data)
    except ValueError as e:
        print(f"Не удалось проинициализировать студента: {e}")
        
test_validate_student()