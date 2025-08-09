import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters



#Тест, что длина пароля соответствует заданной
def test_password_length():
    length = 12
    assert len(generate_password(length)) == length
    length = 20
    assert len(generate_password(length)) == length
    length = 8
    assert len(generate_password(length)) == length
    length = 0
    assert len(generate_password(length)) == length
    length = 50
    assert len(generate_password(length)) == length