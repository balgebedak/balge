from fastapi import FastAPI, Form, Body
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid
from codegen import (
    generate_project,
    plan_project,
    scaffold_structure,
    fill_project,
    autogen_project,
)

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate(prompt: str = Form(...)):
    project_id = str(uuid.uuid4())
    output_path = f"output/{project_id}"
    os.makedirs(output_path, exist_ok=True)

    generate_project(prompt, output_path)

    return JSONResponse({
        "message": "Project generated",
        "output_path": output_path,
    })

@app.get("/view/{project_id}")
def view_main_file(project_id: str):
    file_path = f"output/{project_id}/main.py"
    if not os.path.exists(file_path):
        return JSONResponse({"error": "main.py not found"}, status_code=404)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    return PlainTextResponse(content)

@app.post("/plan")
async def plan(prompt: str = Form(...)):
    plan_result = plan_project(prompt)
    return JSONResponse(plan_result)

@app.post("/scaffold")
async def scaffold_files(plan: dict = Body(...)):
    structure = plan.get("structure")
    if not structure:
        return JSONResponse({"error": "Missing 'structure' in plan"}, status_code=400)
    
    scaffold_structure(structure)
    return JSONResponse({"message": "Project structure created."})

@app.post("/fill")
async def fill_files(payload: dict = Body(...)):
    prompt = payload.get("prompt")
    structure = payload.get("structure")
    if not prompt or not structure:
        return JSONResponse({"error": "Missing 'prompt' or 'structure'"}, status_code=400)
    
    fill_project(prompt, structure)
    return JSONResponse({"message": "Files generated."})

@app.post("/autogen")
async def auto_generate(prompt: str = Form(...)):
    project_id = str(uuid.uuid4())
    output_path = f"output/{project_id}"
    os.makedirs(output_path, exist_ok=True)

    result = autogen_project(prompt, output_path)
    return JSONResponse(result)
