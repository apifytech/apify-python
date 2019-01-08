import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apify",
    version="0.0.2",
    author="Apify Technologies s.r.o.",
    author_email="support@apify.com",
    description="Work in progress: Apify SDK for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apifytech/apify-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

