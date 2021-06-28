import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SpamDetector",
    version="0.0.1",
    author="Marrone Dantas",
    author_email="marrone.dantas@gmail.com",
    description="A small Spam detector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marrone-dantas",
    project_urls={
        "Bug Tracker": "https://github.com/marrone-dantas",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)