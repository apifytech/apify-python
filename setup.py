import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apify_client",
    version="0.0.1",
    author="Apify Technologies s.r.o.",
    author_email="support@apify.com",
    description="Work in progress: Apify API client for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://sdk.apify.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
)

