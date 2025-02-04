from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse
from app.database import engine, SessionLocal
from app.models import Base
from app.routes import listings, map, food_finder

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(listings.router)
app.include_router(map.router)
app.include_router(food_finder.router)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <script src="https://unpkg.com/htmx.org@1.9.2"></script>
        </head>
        <body>
            <h1>Welcome to Scottsdale Tourism App</h1>
            <button hx-get="/update-listings" hx-trigger="click" hx-target="#message">Update Listings</button>
            <div id="message"></div>
        </body>
    </html>
    """
