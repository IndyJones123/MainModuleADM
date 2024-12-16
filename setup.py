from setuptools import setup, find_packages

setup(
    name="MainModuleADM",
    version="0.0.1",
    author="Alfian Dorif Murtadlo",
    author_email="alfianitem999@gmail.com",
    description="A simple logging utility package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
