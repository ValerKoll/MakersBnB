from lib.user_repository import UserRepository
from lib.user import User

"""
calling ALL() 
returns the right list of users
"""
def test_returns_list_of_users(db_connection):
    db_connection.seed("seeds/makersbnb_db_data.sql")
    user_repository = UserRepository(db_connection)
    
    expected = [
        User(1, 'Peter Pan', 'peterpan', 'peter&1234'),
        User(2, 'Jenny Mill', 'notsoFar', 'docker&1234'),
        User(3, 'kevin Tosh', 'kevin-90', 'linux456789!')
        ]
    result = user_repository.all() 
    assert result == expected



"""
calling FIND()
given an USER ID  
returns instance of 1 user
"""
def test_given_user_id_return_user(db_connection):
    db_connection.seed("seeds/makersbnb_db_data.sql")
    user_repository = UserRepository(db_connection)
    
    # corrent user_id return USER class
    username = "notsoFar"
    password = "docker&1234"
    result = user_repository.find(username, password)
    expected = True
    assert expected == result[0]
    expected = "User(2, Jenny Mill, notsoFar, docker&1234)"
    assert expected == str(result[1])
    
    #  not found
    username = "eter"
    password = "peter&12345"
    result = user_repository.find(username, password)
    expected = False
    assert expected == result[0]
    expected = "User not found"
    assert expected == str(result[1])



"""
calling ADD()
given 1 instance of user 
check for DB integrity
  check if valid too
"""
def test_add_1_user_and_check_db(db_connection):
    db_connection.seed("seeds/makersbnb_db_data.sql")
    user_repository = UserRepository(db_connection)
    
    result = user_repository.add(0, "Micheal Bubble", "mike123BUB", "rndnowtv1234")
    expected = True
    assert expected == result[0]
    
    expected = [
    User(1, 'Peter Pan', 'peterpan', 'peter&1234'),
    User(2, 'Jenny Mill', 'notsoFar', 'docker&1234'),
    User(3, 'kevin Tosh', 'kevin-90', 'linux456789!'),
    User(4, "Micheal Bubble", "mike123BUB", "rndnowtv1234")
    ]
    result = user_repository.all() 
    assert expected == result
    
"""
calling ADD()
given an incorrect username and/or incorrect name and/or incorrect password
returns some "error message" accordingly
"""
def test_check_error_messages(db_connection):
    db_connection.seed("seeds/makersbnb_db_data.sql")
    user_repository = UserRepository(db_connection)
    
    result = user_repository.add(0, "Peter Pan", "pn", "password123")
    expected = False
    assert result[0] == expected
    result = ', '.join(result[1])
    expected = "wrong email_address input"
    assert result == expected
    
    result = user_repository.add(1, "Peter Pan", "peter32", "passwo")
    expected = False
    assert result[0] == expected
    result = ', '.join(result[1])
    expected = "wrong password input"
    assert expected == result
    
    result = user_repository.add(1, "Peter Pan", "peter32", "passwordpeter")
    expected = False
    assert result[0] == expected
    result = ', '.join(result[1])
    expected =  "wrong password input"
    assert expected == result

    result = user_repository.add(1, "Peter Pan", "p2", "p2")
    expected = False
    assert result[0] == expected
    result = ', '.join(result[1])
    expected = "wrong email_address input, wrong password input"
    assert expected == result
    
    result = user_repository.add(1, "P2", "p2", "p2")
    expected = False
    assert result[0] == expected
    result = ', '.join(result[1])
    expected = "wrong fullname input, wrong email_address input, wrong password input"
    assert expected == result

