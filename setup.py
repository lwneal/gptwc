from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gptwc",
    version="1.3.0",
    author="Lawrence Neal",
    author_email="nealla@lwneal.com",
    description="A package to count tokens in input text using OpenAI's tiktoken library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lwneal/gptwc",
    packages=find_packages(),
    install_requires=[
        "tiktoken>=0.7.0",
        "pyperclip",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "gptwc=gptwc.gptwc:main",
        ],
    },
)
