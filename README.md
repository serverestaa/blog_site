Open City Blog

Overview

Open City Blog is a full-stack web application designed to manage and publish blog posts. The project is built with a FastAPI backend and a React frontend, with support for image uploads and CRUD operations on blog posts.

Project Structure
```
app/
├── backend/
│   ├── main.py          # FastAPI entry point
│   ├── post.py          # Routes and logic for posts
│   ├── schemas.py       # Pydantic models for request validation
│   ├── database.py      # Database configuration using SQLAlchemy
│   ├── db_post.py       # Database interactions related to posts
│   ├── models.py        # SQLAlchemy ORM models
│   └── requirements.txt # Backend dependencies
└── frontend/
    ├── public/
    │   ├── favicon.jpeg    # Favicon for the app
    │   ├── index.html      # Main HTML file for React app
    │   ├── logo192.png     # 192x192 logo for PWA
    │   ├── logo512.png     # 512x512 logo for PWA
    │   ├── manifest.json   # Metadata for Progressive Web App (PWA)
    │   └── robots.txt      # Search engine crawling configuration
    ├── src/
    │   ├── App.css         # Styling for the main app
    │   ├── App.js          # Main React component
    │   ├── NewPost.js      # Component for creating new posts
    │   ├── Post.js         # Component for displaying individual posts
    │   ├── index.js        # ReactDOM entry point
    └── package.json        # Frontend dependencies
```
Features

	•	FastAPI Backend: A fast and asynchronous backend powered by FastAPI, handling blog posts with full CRUD operations.
	•	React Frontend: A responsive React.js frontend, allowing users to view, create, and delete blog posts.
	•	Image Uploads: Users can upload images along with their posts.
	•	Progressive Web App (PWA): The frontend supports PWA features, including installation on mobile and desktop devices.
	•	Post Management: Create, Read, and Delete posts functionality.

Tech Stack

	•	Backend: FastAPI, SQLAlchemy, Pydantic
	•	Frontend: React, JavaScript
	•	Database: SQLite (or any SQLAlchemy-supported DB)
	•	Hosting: Localhost (can be configured for cloud deployment)

Getting Started

Prerequisites

	•	Python 3.x
	•	Node.js and npm (for frontend)

Backend Setup

1.	Navigate to the backend directory:
```
cd app/backend
```

2.	Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3.	Install backend dependencies:
```
pip install -r requirements.txt
```

4.	Run the FastAPI server:
```
uvicorn main:app --reload
```
This starts the backend server at http://localhost:8000.

Frontend Setup

1.	Navigate to the frontend directory:
```
cd app/frontend
```

2.	Install frontend dependencies:
```
npm install
```

3.	Start the React app:
```
npm start
```
This starts the frontend at http://localhost:3000.

API Endpoints

	•	GET /post/all: Fetch all posts.
	•	POST /post: Create a new post.
	•	DELETE /post/{id}: Delete a post by ID.
	•	POST /post/image: Upload an image for a post.

Creating Posts

	1.	Open the app at http://localhost:3000.
	2.	Use the “Create Post” form to submit a new post with an optional image.
	3.	Posts will be displayed in reverse chronological order.

Available Scripts (Frontend)

In the frontend/ directory, you can run:

	•	npm start: Runs the app in the development mode.
	•	npm test: Launches the test runner.
	•	npm run build: Builds the app for production.
	•	npm run eject: Remove the single build dependency from your project.

License

This project is open-source and available under the MIT License.

Contributing

Feel free to submit issues or pull requests to improve the project.
