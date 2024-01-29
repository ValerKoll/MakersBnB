from lib.user import User


"""
give a correct id, name, username and password
returns true and store a correct instance
"""
def test_give_right_parameters():
    user = User(1, "Peter Pan", "petpan", "password123")
    assert str(user) == "User(1, Peter Pan, petpan, password123)"
    user = User(1, "Peter Pan", "petpan", "password%!3")
    assert str(user) == "User(1, Peter Pan, petpan, password%!3)"

"""
give 2 instance of user
returns true if the 2 instances contains same values
"""
def test_give_2_instances_compare_result():
    user1 = User(1, "Peter Pan", "petpan", "password123")
    user2 = User(1, "Peter Pan", "petpan", "password123")
    assert (user1 == user2) == True

"""
give an incorrect username and/or incorrect name and/or incorrect password
returns False or True accordingly
"""
def test_incorrent_username_and_or_password():
    # check (len >= 3 & <= 12), (alphanumeric chars only), (later stage: unique)
    #
    #username too short
    user = User(1, "Peter Pan", "pn", "password123")
    assert user.is_valid() == False
    assert bool("wrong email_address input" in user.errors) == True
    #username start with 1 digit 
    user = User(1, "Peter Pan", "1eter32", "password32")
    assert user.is_valid() == False
    #correct input
    user = User(1, "Peter Pan", "peter32", "passw£!?d123")
    assert user.is_valid() == True
    #username too long
    user = User(1, "Peter Pan", "peter32morethan12", "passw£!?d123")
    assert user.is_valid() == False
    #username correct, password incorret
    user = User(1, "Peter Pan", "peter32", "passw£-(123")
    assert user.is_valid() == False
    #username correct, password incorret - no digit
    user = User(1, "Peter Pan", "peter32", "passwordpswd")
    assert user.is_valid() == False
"""
give a name or a username with an empty space at the begining or the end
returns username without spaces
"""
def test_remove_empty_spaces():
    user = User(1, "  Peter Pan ", " peter23 ", "password123")
    assert user.fullname  == "Peter Pan"
    assert user.email_address  == "peter23"

"""
given empty name or too short name <3
return None
"""
def test_check_name_too_short():
    user = User(1, "", "peter23", "password£123")
    assert user.is_valid() == False
    user = User(1, "Pe", "peter23", "password£123")
    assert user.is_valid() == False

"""
give an username with an empty space in between 2+ words
check for an input with a single word
returns False
"""
def test_reject_empty_spaces_in_between():
    # peter _space_ 23 not be accepted
    user = User(1, "Peter Pan", " peter 23 ", "password123")
    assert user.is_valid()  == False
    # peter23 with not space ==> ok
    user = User(1, "Peter Pan", " peter23 ", "password123")
    assert user.is_valid()  == True

"""
give an password with:
    wrong chars,
    too short or too long, 3< >12
    only alpha/numbers and...
    including special chars without '%','&','!','?'
    not containing at least 2+ digit
returns False
"""
def test_given_wrong_password():
    # too short
    user = User(1, "Peter Pan", "peter23", "pa")
    assert user.is_valid() == False
    # too long
    user = User(1, "Peter Pan", "peter23", "passwordtoolongtoolong")
    assert user.is_valid() == False
    # with special chars present
    user = User(1, "Peter Pan", "peter23", "password123")
    assert user.is_valid() == True
    # special chars but not digits
    user = User(1, "Peter Pan", "peter23", "password&?£!")
    assert user.is_valid() == False

