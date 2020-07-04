import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lua-py-buffhorse", # Replace with your own username
    version="1",
    author="buff horse",
    author_email=" ",
    description="test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BuffHorse/LuaPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
