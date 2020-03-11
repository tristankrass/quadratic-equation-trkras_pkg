import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qequation-trkras-pkg",
    version="0.0.1",
    author="Tristan Krass",
    author_email="tristan@tristan.ee",
    description="Quadratic equation solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tristankrass/quadratic-equation-trkras_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)