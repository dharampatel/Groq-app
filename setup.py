from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Groq_App",
    version="1.0",
    author="Dharmendra",
    packages=find_packages(),
    install_requires = requirements,
)