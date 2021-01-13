import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spow-YapperMags", # Replace with your own username
    version="1.0.0",
    author="Magnus Peterson-Munoz",
    author_email="magnuspetersonmunoz@gmail.com",
    description="A PowerShell like tool made with the OS Module.",
    long_description='README.md',
    long_description_content_type="text/markdown",
    url="https://github.com/LIKE-Productions/spow",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD 3-Clasue License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)