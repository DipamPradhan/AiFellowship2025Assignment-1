# 🎬 Movie Finder API

Search for movies and fetch detailed information using the OMDb API. Built with FastAPI and ready for local use or containerized deployment via Docker.

---

## 🚀 Features

- 🔎 Search for movies by title
- 🎥 Get title, year, genre, director, plot, IMDb rating, and poster
- 🧠 Built with FastAPI
- 🐳 Fully Dockerized

---

## 📦 Requirements

> For Local Use:

- Python 3.10+
- pip

> For Docker Use:

- Docker
- Docker Compose

---

## 📁 .env Configuration

Create a `.env` file in the project root with the following:

```env
omdb_api_key=your_omdb_api_key_here
APP_HOST=0.0.0.0
APP_PORT=5000
```

Get your free OMDb API key at (http://www.omdbapi.com/apikey.aspx)

---

## 💻 Run Locally

```bash
git clone https://github.com/DipamPradhan/AiFellowship2025Assignment-1.git
cd moviefinder

# Create virtual environment
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python -m moviefinder.app
```

Open your browser and go to [http://localhost:5000](http://localhost:5000)

---

## 🐳 Run with Docker

```bash
git clone https://github.com/DipamPradhan/AiFellowship2025Assignment-1.git
cd moviefinder

docker-compose up --build
```

Open your browser and go to [http://localhost:5000](http://localhost:5000)
For usability go to (http://localhost:5000/docs)

---

## 📖 API Usage

- Root endpoint `/`
  Returns a welcome message.

- Movie search `/movie?title=MovieTitle`
  Replace `MovieTitle` with your desired movie name.

Example:

```
http://localhost:5000/movie?title=Inception
```

---

## ⚙️ Environment Variables Used

| Variable     | Description                  | Default         |
| ------------ | ---------------------------- | --------------- |
| omdb_api_key | Your OMDb API key (required) | None (required) |
| APP_HOST     | Host for the FastAPI server  | 0.0.0.0         |
| APP_PORT     | Port for the FastAPI server  | 5000            |

---

## 🧹 Development Notes

- Code style follows PEP8
- Pre-commit hooks available for linting and formatting (optional)
- Use `uvicorn` or the provided run script to start the server

---

Developed by Dipam Pradhan
