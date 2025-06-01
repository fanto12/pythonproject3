from setuptools import setup

setup(
    name="pythonproject3",
    version="0.1",
    py_modules=["app"],  # refers to app.py in the root directory
    install_requires=[],  # list your dependencies here, e.g. ["requests", "numpy"]
    author="Your Name",  # optional but recommended
    author_email="your.email@example.com",  # optional but recommended
    description="A short description of your project",  # optional but recommended
    url="https://github.com/your-username/your-repo",  # optional but recommended
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Change if you use a different license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify your Python version compatibility
)
