# integrationTest.py

import pytest
from fastapi.testclient import TestClient
from main import app, SessionLocal, Base, engine
from sqlalchemy.orm import sessionmaker

# Test setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_library.db"
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
client = TestClient(app)

# Create a test database
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Test cases
def test_create_borrowlist():
    # Create a user
    response = client.post("/users/", json={"username": "testuser", "fullname": "Test User"})
    assert response.status_code == 422
    user_data = response.json()
    print("Create User Response:", user_data)  # Debugging print
    assert "id" in user_data
    user_id = user_data["id"]

    # Create a book
    response = client.post("/books/", json={"title": "Test Book", "firstauthor": "Author", "isbn": "1234567890"})
    assert response.status_code == 422
    book_data = response.json()
    print("Create Book Response:", book_data)  # Debugging print
    assert "id" in book_data
    book_id = book_data["id"]

    # Create a borrow list entry
    response = client.post("/borrowlist/", json={"user_id": user_id, "book_id": book_id})
    assert response.status_code == 422
    borrowlist_data = response.json()
    print("Create Borrowlist Response:", borrowlist_data)  # Debugging print
    assert borrowlist_data["user_id"] == user_id
    assert borrowlist_data["book_id"] == book_id

def test_get_borrowlist():
    # Create a user
    response = client.post("/users/", json={"username": "testuser2", "fullname": "Test User 2"})
    assert response.status_code == 422
    user_data = response.json()
    print("Create User Response:", user_data)  # Debugging print
    assert "id" in user_data
    user_id = user_data["id"]

    # Create a book
    response = client.post("/books/", json={"title": "Test Book 2", "firstauthor": "Author 2", "isbn": "0987654321"})
    assert response.status_code == 422
    book_data = response.json()
    print("Create Book Response:", book_data)  # Debugging print
    assert "id" in book_data
    book_id = book_data["id"]

    # Create a borrow list entry
    client.post("/borrowlist/", json={"user_id": user_id, "book_id": book_id})

    # Retrieve the borrow list
    response = client.get(f"/borrowlist/{user_id}")
    assert response.status_code == 422
    borrowlist_data = response.json()
    print("Get Borrowlist Response:", borrowlist_data)  # Debugging print
    assert len(borrowlist_data) == 1
    assert borrowlist_data[0]["book_id"] == book_id

if __name__ == "__main__":
    pytest.main()
