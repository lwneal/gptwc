from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gptwc",
    version="1.1.0",
    author="Lawrence Neal",
    author_email="nealla@lwneal.com",
    description="A package to count tokens in input text using OpenAI's tiktoken library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lwneal/gptwc",
    packages=find_packages(),
    install_requires=[
        "tiktoken",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "gptwc=gptwc.gptwc:main",
        ],
    },
)
