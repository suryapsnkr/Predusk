def test_create_review():
    # Create a book first
    book = client.post("/books", json={
        "title": "Another Book", "author": "Author Y", "published_date": "2021"
    }).json()

    # Create a review
    response = client.post(f"/books/{book['id']}/reviews", json={
        "rating": 5, "review_text": "Excellent!"
    })
    assert response.status_code == 200
    assert response.json()["rating"] == 5
