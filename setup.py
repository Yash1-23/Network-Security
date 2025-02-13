from setuptools import setup, find_packages

def get_requirements():
    """Reads the requirements.txt file and returns a list of dependencies."""
    try:
        with open("requirements.txt", "r", encoding="utf-8") as file:
            requirements = [line.strip() for line in file if line.strip() and not line.startswith("-e .")]
        return requirements
    except FileNotFoundError:
        print("Warning: requirements.txt file not found.")
        return []

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Yashwanth Singh",
    author_email="yashwanthsinghgarandal@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
