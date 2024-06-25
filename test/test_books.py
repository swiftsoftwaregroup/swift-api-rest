import pytest

from fastapi.testclient import TestClient

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from swift_api_rest.models_db import Base, BookModel
from swift_api_rest.app import app, get_db

# use in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite://"

# use ./test.db SQLite database for testing
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def test_fixture():
    # create tables
    Base.metadata.create_all(bind=engine)
    
    # override the get_db dependency
    app.dependency_overrides[get_db] = override_get_db
    
    client = TestClient(app)
    yield client
    
    # Clean up
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(autouse=True)
def clean_table(test_fixture):
    db = TestingSessionLocal()
    db.query(BookModel).delete()
    db.commit()

def test_create_book(test_fixture):
    response = test_fixture.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "date_published": "2024-06-24", "cover_image": "http://example.com/cover.jpg"}
    )
    assert response.status_code == 200
    
    data = response.json()
    assert data["title"] == "Test Book"
    assert data["author"] == "Test Author"
    assert data["date_published"] == "2024-06-24"
    assert data["cover_image"] == "http://example.com/cover.jpg"
    assert "id" in data


def test_read_books(test_fixture):
    test_fixture.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "date_published": "2024-06-24", "cover_image": "http://example.com/cover.jpg"}
    )
    
    response = test_fixture.get("/books/")
    assert response.status_code == 200

    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Test Book"


def test_read_book(test_fixture):
    create_response = test_fixture.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "date_published": "2024-06-24", "cover_image": "http://example.com/cover.jpg"}
    )
    book_id = create_response.json()["id"]
    
    response = test_fixture.get(f"/books/{book_id}")
    assert response.status_code == 200
    
    data = response.json()
    assert data["title"] == "Test Book"


def test_update_book(test_fixture):
    create_response = test_fixture.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "date_published": "2024-06-24", "cover_image": "http://example.com/cover.jpg"}
    )
    book_id = create_response.json()["id"]
    
    response = test_fixture.put(
        f"/books/{book_id}",
        json={"title": "Updated Book", "author": "Updated Author", "date_published": "2023-02-01", "cover_image": "http://example.com/updated_cover.jpg"}
    )
    assert response.status_code == 200
    
    data = response.json()
    assert data["title"] == "Updated Book"
    assert data["author"] == "Updated Author"
    assert data["date_published"] == "2023-02-01"
    assert data["cover_image"] == "http://example.com/updated_cover.jpg"


def test_delete_book(test_fixture):
    create_response = test_fixture.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author", "date_published": "2024-06-24", "cover_image": "http://example.com/cover.jpg"}
    )
    book_id = create_response.json()["id"]
    
    response = test_fixture.delete(f"/books/{book_id}")
    assert response.status_code == 200
    
    # try to get the deleted book
    get_response = test_fixture.get(f"/books/{book_id}")
    assert get_response.status_code == 403

def test_read_non_existent_book(test_fixture):
    # assuming 1099 is a non-existent id
    response = test_fixture.get("/books/1099") 
    assert response.status_code == 404


def test_update_non_existent_book(test_fixture):
    # assuming 1099 is a non-existent id
    response = test_fixture.put(
        "/books/1099",
        json={"title": "Updated Book", "author": "Updated Author", "date_published": "2023-02-01", "cover_image": "http://example.com/updated_cover.jpg"}
    )
    assert response.status_code == 404


def test_delete_non_existent_book(test_fixture):
    # assuming 1099 is a non-existent id
    response = test_fixture.delete("/books/1099")
    assert response.status_code == 404
