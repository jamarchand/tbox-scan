import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tbox-scan", # Replace with your own username
    version="0.5",
    author="Jorge A. Marchand",
    author_email="marchand@hms.harvard.edu",
    description="A package for finding T-boxes in FASTA sequences",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jamarchand/tbox-scan",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)