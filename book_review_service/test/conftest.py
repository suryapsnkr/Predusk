def test_cache_miss(monkeypatch):
    from app.cache import r

    # Simulate cache miss
    monkeypatch.setattr(r, "get", lambda *a, **kw: None)

    response = client.get("/books/")
    assert response.status_code == 200
