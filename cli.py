import os
import argparse
from pathlib import Path
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def display_intro():
    """Display an introduction about the developer."""
    print(Fore.CYAN + "===========================================")
    print(Fore.GREEN + "Welcome to Django-Ahin!")
    print(Fore.CYAN + "===========================================")
    print(Fore.YELLOW + "This tool helps you quickly generate Django projects with apps,")
    print(Fore.YELLOW + "including templates, static files, models, and forms.")
    print(Fore.CYAN + "===========================================")
    print(Fore.MAGENTA + "Created by: Your Name")
    print(Fore.MAGENTA + "Email: your.email@example.com")
    print(Fore.MAGENTA + "GitHub: https://github.com/yourusername")
    print(Fore.CYAN + "===========================================")
    print(Style.RESET_ALL)

def create_project(project_name, app_name):
    """Create a Django project and app with templates and static files."""
    print(Fore.BLUE + f"Creating Django project: {project_name}...")
    os.system(f"django-admin startproject {project_name}")

    # Navigate into the project directory
    os.chdir(project_name)

    print(Fore.BLUE + f"Creating Django app: {app_name}...")
    os.system(f"python manage.py startapp {app_name}")

    # Create directories for static files and templates
    os.makedirs(f"{app_name}/static/css", exist_ok=True)
    os.makedirs(f"{app_name}/static/js", exist_ok=True)
    os.makedirs(f"{app_name}/templates/", exist_ok=True)

    # Create static files
    with open(f"{app_name}/static/css/styles.css", "w") as f:
        f.write("/* Add your CSS here */")

    with open(f"{app_name}/static/js/scripts.js", "w") as f:
        f.write("// Add your JavaScript here")

    # Create template files
    templates = {
        "base.html": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Site{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'app_name/css/styles.css' %}">
</head>
<body>
    <header>
        <h1>Welcome to My Site</h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <script src="{% static 'app_name/js/scripts.js' %}"></script>
</body>
</html>
        """,
        "index.html": """
{% extends 'app_name/base.html' %}

{% block title %}Home{% endblock %}

{% block content %}
    <h2>Home Page</h2>
    <p>Welcome to the home page!</p>
{% endblock %}
        """,
        "detail.html": """
{% extends 'app_name/base.html' %}

{% block title %}Detail{% endblock %}

{% block content %}
    <h2>Detail Page</h2>
    <p>This is the detail page.</p>
{% endblock %}
        """,
    }

    for filename, content in templates.items():
        with open(f"{app_name}/templates/{filename}", "w") as f:
            f.write(content)

    # Add the app to INSTALLED_APPS in settings.py
    with open(f"{project_name}/settings.py", "a") as f:
        f.write(f"\nINSTALLED_APPS += ['{app_name}']\n")

    print(Fore.GREEN + f"Successfully created Django project '{project_name}' with app '{app_name}'.")
    print(Fore.CYAN + "===========================================")
    print(Fore.YELLOW + "Next steps:")
    print(Fore.YELLOW + f"1. Navigate to the project directory: cd {project_name}")
    print(Fore.YELLOW + "2. Run migrations: python manage.py migrate")
    print(Fore.YELLOW + "3. Start the development server: python manage.py runserver")
    print(Fore.CYAN + "===========================================")

def main():
    """Main function to handle command-line arguments."""
    display_intro()  # Display the introduction
    parser = argparse.ArgumentParser(description="Generate a Django project with an app.")
    parser.add_argument("project_name", help="Name of the Django project")
    parser.add_argument("app_name", help="Name of the Django app")
    args = parser.parse_args()

    create_project(args.project_name, args.app_name)

if __name__ == "__main__":
    main()