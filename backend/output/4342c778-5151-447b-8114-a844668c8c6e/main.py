import os

# Create directory structure
directories = [
    "backend/app/routers",
    "backend/app/models",
    "backend/app/schemas",
    "backend/app/services",
    "frontend/src/components",
    "frontend/src/pages",
    "frontend/src/services",
    "frontend/src/context"
]

for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create main.py
with open("backend/app/main.py", "w") as f:
    f.write("""from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
""")

# Create database.py
with open("backend/app/database.py", "w") as f:
    f.write("""# Database connection setup
""")

# Create .env.example
with open(".env.example", "w") as f:
    f.write("""# Example environment variables
DATABASE_URL=postgresql://user:password@localhost/dbname
""")

# Create README.md
with open("README.md", "w") as f:
    f.write("""# Project Title

## Description
A brief description of the project.

## Installation
Instructions to install the project.

## Usage
Instructions on how to use the project.
""")

# Create keep files
keep_files = [
    "backend/app/routers/.keep",
    "backend/app/models/.keep",
    "backend/app/schemas/.keep",
    "backend/app/services/.keep",
    "frontend/src/components/.keep",
    "frontend/src/pages/.keep",
    "frontend/src/services/.keep",
    "frontend/src/context/.keep"
]

for keep_file in keep_files:
    with open(keep_file, "w") as f:
        f.write("# Keep this directory") 

# Create index.js
with open("frontend/src/index.js", "w") as f:
    f.write("""import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));
""")

# Create App.js in the frontend src
with open("frontend/src/App.js", "w") as f:
    f.write("""import React from 'react';

function App() {
    return (
        <div>
            <h1>Hello World</h1>
        </div>
    );
}

export default App;
""")