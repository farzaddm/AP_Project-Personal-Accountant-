from Utils.validation import Validation

v = Validation()


def test_phone_validation() -> None:
    assert v.validate_phone("091347852") == False
    assert v.validate_phone("09132546531") == True
    assert v.validate_phone("+98 9137485423") == False
    assert v.validate_phone("9137493655") == False


def test_email_validation() -> None:
    assert v.validate_email("1@gmail.com") == True
    assert v.validate_email("1df#gmail.com") == False
    assert v.validate_email("G1@.com") == False
    assert v.validate_email("qw@spo&@yaHoO.com") == False
    assert v.validate_email("1@yahoo.com") == True
    assert v.validate_email("12w@gmail.cm") == False
    assert v.validate_email("@gmail.com") == False


def test_name_validation() -> None:
    assert v.validate_name("mmd") == True
    assert v.validate_name("mm d") == True
    assert v.validate_name("12") == False
    assert v.validate_name("1wq2") == False


def test_username_validation() -> None:
    assert v.validate_username("") == False


def test_password_validation() -> None:
    assert v.validate_password("125g") == False
    assert v.validate_password("125458") == False
    assert v.validate_password("12G458") == False
    assert v.validate_password("sFgl&*#g") == False
    assert v.validate_password("1sFgl&*#g") == True


def test_birthday_validation() -> None:
    assert v.validate_birthday("1990-12-5") == True
    assert v.validate_birthday("1890-12-5") == False
    assert v.validate_birthday("2890-12-5") == False


def test_category_validation() -> None:
    assert v.validate_category("dhlf3F") == True
    assert v.validate_category("#$!") == False
    assert v.validate_category("") == False


def test_source_validation() -> None:
    assert v.validate_source_of_price("") == False


def test_type_validation() -> None:
    assert v.validate_type_of_price("") == False


