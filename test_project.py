from project import validate_mobile, validate_stud_email, validate_password


def test_validate_mobile():
    assert validate_mobile("+27") == False
    assert validate_mobile("+27677007812") == True


def test_validate_stud_email():
    assert validate_stud_email("zee@") == False
    assert validate_stud_email("zeelovescupcakes@gmail.com") == False
    assert validate_stud_email("iamziccokavie@gmail.com") == True


def test_validate_password():
    assert validate_password("star") == False
    assert validate_password("alxproject") == False
    assert validate_password("password-") == True
