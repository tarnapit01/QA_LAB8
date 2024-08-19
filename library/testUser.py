# Lab8 - Integration testing
# Unit test -> class User in main.py

import pytest
from main import User, Book

# uses the db_session fixture inside conftest.py
def test_add_user(db_session):
    new_user = User(username = "test1",fullname = "thanaphat", has_book = True)
    db_session.add(new_user)
    db_session.commit()
    
    user = db_session.query(User).filter_by(username = "test1").first()
    assert user is not None
    assert user.username == "test1"
    
    
def test_delete_user(db_session):
    # Add a user, then remove this new user from the db
    user = User(username = "test2",fullname = "thanaphat03", has_book = True)
    db_session.add(user)
    db_session.commit()

    # Delete the test_newuser2
    db_session.delete(user)
    db_session.commit()

    # Query the test_newuser2 to check if it is removed from the db
    deleted_user = db_session.query(User).filter_by(username="test2").first()
    assert deleted_user is None

def test_add_book(db_session):
     # Add a user, then remove this new user from the db
    book = Book(title = "book2",firstauthor = "thanaphat03", isbn = "True")
    db_session.add(book)
    db_session.commit()

    # Delete the Book2
    db_session.delete(book)
    db_session.commit()


def test_dalete_book(db_session):
     # Add a user, then remove this new user from the db
    book = Book(title = "book3",firstauthor = "thanaphat04", isbn = "False")
    db_session.add(book)
    db_session.commit()

    # Delete the Book3
    db_session.delete(book)
    db_session.commit()
