# Scottsdale Tourism App

This project is a FastAPI-based web application that provides a map of Scottsdale with tourist points of interest, a food finder, and live home listings for sale in the area.

## Setup Instructions

### Prerequisites
- Docker & Docker Compose installed
- Python 3.10+

### Running the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/scottsdale-tourism-app.git
   cd scottsdale-tourism-app
   ```
2. Create a `.env` file and update database credentials (already provided in this repo).
3. Build and run the application with Docker Compose:
   ```sh
   docker-compose up --build
   ```
4. Access the application at `http://localhost:8000`

### Endpoints
- `/update-listings` - Triggers background update of home listings
- `/` - Main page with interactive map and food finder

### Tech Stack
- **Backend**: FastAPI, PostgreSQL, SQLAlchemy
- **Frontend**: HTMX, Jinja2, Leaflet.js (for maps)
- **Deployment**: Docker, Docker Compose

### Future Improvements
- Add Redis and Celery for better background task handling
- Implement user authentication if needed
