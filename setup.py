import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TriTest",
    version="0.0.1",
    author="Niclas Eriksson",
    author_email="niclas@eriksson.cc",
    description="Test REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/goliat_43/TriTest",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "tri_test"},
    packages=setuptools.find_packages(where="tri_test"),
    python_requires=">=3.8",
)