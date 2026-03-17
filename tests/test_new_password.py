import string
from password.new_password import generate_password

def test_generate_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_generate_password_length():
    password_length = 12
    assert len(generate_password(password_length)) == password_length
    password_length = 500
    assert len(generate_password(password_length)) == password_length
    password_length = 1000
    assert len(generate_password(password_length)) == password_length
    password_length = 35
    assert len(generate_password(password_length)) == password_length
    password_length = 0
    assert len(generate_password(password_length)) == password_length
    password_length = -5
    assert len(generate_password(password_length)) == 0
    
def test_generate_password_uniqueness():
    password1 = generate_password(12)
    password2 = generate_password(12)
    assert password1 != password2    

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""
