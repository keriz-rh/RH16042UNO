from setuptools import setup, find_packages

setup(
    name="RH16042UNO",
    version="0.1.0",
    description="Librería para resolver sistemas de ecuaciones lineales y no lineales",
    author="Kevin Rivera",
    author_email="rh16042@ues.edu.sv",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.19.0",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)