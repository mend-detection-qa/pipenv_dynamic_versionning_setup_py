from setuptools import setup, find_packages

setup(
    name="example-project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests==2.32.4",
    ],
    python_requires=">=3.7",
)
