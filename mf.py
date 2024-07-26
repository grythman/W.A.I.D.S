import os

# Бүтцийн модыг тодорхойлно
structure = {
    "backend": {
        "manage.py": "",
        "backend": {
            "__init__.py": "",
            "settings.py": "",
            "urls.py": "",
            "wsgi.py": ""
        },
        "journal": {
            "__init__.py": "",
            "admin.py": "",
            "apps.py": "",
            "models.py": "",
            "views.py": "",
            "urls.py": "",
            "serializers.py": ""
        },
        "templates": {
            "index.html": ""
        }
    },
    "frontend": {
        "public": {
            "index.html": "",
            "favicon.ico": ""
        },
        "src": {
            "App.js": "",
            "index.js": "",
            "components": {
                "Login.js": "",
                "Register.js": "",
                "Dashboard.js": "",
                "Journal.js": "",
                "Feedback.js": ""
            },
            "styles": {
                "App.css": "",
                "index.css": ""
            }
        },
        "package.json": "",
        "package-lock.json": ""
    },
    "README.md": "",
    ".gitignore": ""
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, 'w') as file:
                file.write(content)

# Үндсэн хавтас
base_path = "internship-journal"
os.makedirs(base_path, exist_ok=True)

# Бүтцийг үүсгэнэ
create_structure(base_path, structure)

print(f"The structure has been created at {os.path.abspath(base_path)}")
