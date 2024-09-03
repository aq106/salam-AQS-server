from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Create necessary directories if they don't exist
os.makedirs("static/css", exist_ok=True)
os.makedirs("static/js", exist_ok=True)
os.makedirs("templates", exist_ok=True)

# Mount the static files directory to serve CSS, JS, images, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates directory
templates = Jinja2Templates(directory="templates")

# Define route to serve HTML template
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Generate example HTML template if it doesn't exist
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AQS Ecommerce</title>
    <link rel="stylesheet" href="/static/css/styles.css">
</head>
<body>
    <h1>Welcome to AQS Ecommerce</h1>
    <p>This is a simple static web app using FastAPI.</p>
    <script src="/static/js/scripts.js"></script>
</body>
</html>
"""

if not os.path.exists("templates/index.html"):
    with open("templates/index.html", "w") as f:
        f.write(html_content)

# Generate example CSS if it doesn't exist
css_content = """
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    text-align: center;
}

h1 {
    color: #007bff;
}
"""

if not os.path.exists("static/css/styles.css"):
    with open("static/css/styles.css", "w") as f:
        f.write(css_content)

# Generate example JavaScript if it doesn't exist
js_content = """
console.log("JavaScript is loaded!");
"""

if not os.path.exists("static/js/scripts.js"):
    with open("static/js/scripts.js", "w") as f:
        f.write(js_content)
