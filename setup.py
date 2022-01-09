import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

VERSION = "0.0.1"

setuptools.setup(
    name="Meaning of Life",
    version=VERSION,
    author="NathanielChavdarov",
    author_email="",
    description="It's 42",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NathanielChavdarov/cython-test-app",
    packages=setuptools.find_packages(),
    package_data={"meaningoflife": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
    install_requires=[],
    setup_requires=["wheel"],
    zip_safe=False,
)
