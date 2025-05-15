from httpx import ASGITransport, AsyncClient
import pytest

from moviefinder.app import app


@pytest.mark.asyncio
async def test_root_should_return_welcome_message():
    """
    Test the root '/' endpoint.
    - Should return status code 200.
    - Should contain 'Movie Finder API' in the response message.
    """
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "Movie Finder API" in response.json()["message"]


@pytest.mark.asyncio
async def test_movie_should_return_mocked_inception(monkeypatch):
    async def mock_get(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.status_code = 200

            def json(self):
                return {
                    "Title": "Inception",
                    "Year": "2010",
                    "Genre": "Action, Adventure, Sci-Fi",
                    "Director": "Christopher Nolan",
                    "Plot": "A thief who steals corporate secrets...",
                    "imdbRating": "8.8",
                    "Poster": "https://example.com/inception.jpg",
                    "Response": "True",
                }

        return MockResponse()

    monkeypatch.setattr("httpx.AsyncClient.get", mock_get)

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/movie", params={"title": "Inception"})

    assert response.status_code == 200
    assert response.json()["Title"] == "Inception"
