import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_project(prompt: str, output_path: str):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert Python developer. "
                        "Generate a complete, clean, and runnable Python script. "
                        "Do not include explanations or markdown."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )

        code = response.choices[0].message.content

        os.makedirs(output_path, exist_ok=True)
        with open(os.path.join(output_path, "main.py"), "w", encoding="utf-8") as f:
            f.write(code)

    except Exception as e:
        print("🔥 ERROR in generate_project:", e)
        raise

def plan_project(prompt: str) -> dict:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a senior software architect. Based on the user's app idea, "
                        "return a JSON plan with:\n"
                        "1. project_type\n"
                        "2. tech_stack\n"
                        "3. features\n"
                        "4. needs\n"
                        "5. entry_file\n"
                        "6. structure\n"
                        "Only valid JSON. No markdown or explanations."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )

        return json.loads(response.choices[0].message.content)

    except json.JSONDecodeError:
        return {"error": "Invalid JSON returned from OpenAI"}
    except Exception as e:
        print("🔥 ERROR in plan_project:", e)
        return {"error": str(e)}

def scaffold_structure(structure: dict, base_path: str = "output/temp"):
    """Creates folders and empty files based on the nested structure dict."""
    def extract_paths(tree, prefix=""):
        paths = []
        for name, content in tree.items():
            path = os.path.join(prefix, name)
            if isinstance(content, dict):
                paths += extract_paths(content, path)
            else:
                paths.append(path)
        return paths

    paths = extract_paths(structure)

    for path in paths:
        full_path = os.path.join(base_path, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write("")
        print(f"📁 Created: {full_path}")

def fill_project(prompt: str, structure: dict, base_path: str = "output/temp"):
    """Fills each file path with AI-generated content."""
    def extract_paths(tree, prefix=""):
        paths = []
        for name, content in tree.items():
            path = os.path.join(prefix, name)
            if isinstance(content, dict):
                paths += extract_paths(content, path)
            else:
                paths.append(path)
        return paths

    file_paths = extract_paths(structure)

    for file_path in file_paths:
        abs_path = os.path.join(base_path, file_path)
        os.makedirs(os.path.dirname(abs_path), exist_ok=True)

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini-2024-07-18",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert fullstack developer. Based on the user's app idea, "
                            f"generate only the content of this file:\n{file_path}\n"
                            "No markdown. Just code. Follow best practices."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.3,
            )

            code = response.choices[0].message.content.strip()
            with open(abs_path, "w", encoding="utf-8") as f:
                f.write(code)
            print(f"✅ Wrote: {file_path}")

        except Exception as e:
            print(f"❌ Failed to write {file_path}:", e)

def autogen_project(prompt: str, output_path: str):
    """Does plan → scaffold → fill automatically."""
    try:
        plan = plan_project(prompt)
        structure = plan.get("structure")
        if not structure:
            return {"error": "Missing 'structure' in plan result."}

        scaffold_structure(structure, output_path)
        fill_project(prompt, structure, output_path)

        return {"message": "Full project generated", "structure": structure, "output_path": output_path}

    except Exception as e:
        print("🔥 ERROR in autogen_project:", e)
        return {"error": str(e)}
