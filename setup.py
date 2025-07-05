from setuptools import setup, find_packages

setup(
    name="Procokies",  # your package name
    version="1.0.0",
    author="PROOTAKU2",
    description="Central cookies handler for telegram music bots",
    packages=find_packages(),  # Automatically detect packages
    include_package_data=True,  # Include non-code files specified in MANIFEST.in
    package_data={
        "Procokies": ["cookies.txt"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
