from fastapi import FastAPI, Query, HTTPException
import httpx
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Load OMDb API key from environment variables
OMDB_API_KEY = os.getenv("omdb_api_key")


"""
GET /
----------
This is the root route of the Movie Finder API.

Usage:
- Returns a welcome message and instructions on how to use the API.

Parameters:
- None

Returns:
- A simple JSON message with usage guidance.
"""


@app.get("/")
def root():
    return {
        "message": "Welcome to the Movie Finder API. Use /movie?title=YourTitle to search."
    }


"""
GET /movie
----------
Fetches movie details from the OMDb API based on the title provided as a query parameter.

Usage:
- Send a GET request to /movie?title=<movie_title>
- Uses the title to query the OMDb API

Parameters:
- title (str): The movie title to search for. Required.

Returns:
- A JSON object with selected movie details such as title, year, genre, director, plot, IMDb rating, and poster URL.

Raises:
- HTTPException (404): If the movie is not found or the OMDb API returns an error.
"""


@app.get("/movie")
async def get_movie(title: str = Query(..., description="Movie title to search")):
    """
    Parameters:- title (str): The movie title to search for. Required.
    """
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        movie = response.json()

    if movie.get("Response") == "False":
        raise HTTPException(
            status_code=404, detail=movie.get("Error", "Movie not found")
        )

    return {
        "title": movie["Title"],
        "year": movie["Year"],
        "genre": movie["Genre"],
        "director": movie["Director"],
        "plot": movie["Plot"],
        "imdb_rating": movie["imdbRating"],
        "poster": movie["Poster"],
    }
