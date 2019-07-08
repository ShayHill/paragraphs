import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='docx2python',
    version='1.0',
    author="Shay Hill",
    author_email="shay_public@hotmail.com",
    description="Incorporate long strings painlessly, beautifully into Python code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ShayHill/paragraphs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
