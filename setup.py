from setuptools import setup, find_packages

setup(
    name="forestsentinel",
    version="0.1.0",
    description="Satellite-based deforestation monitoring tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Arun Kumar Pandey",
    author_email="arunp77@gmail.com",
    url="https://github.com/arunp77/forestsentinel",
    packages=find_packages(),
    install_requires=[
        "pyspark>=3.0.0",
        "rasterio>=1.2.0",
        "geopandas>=0.9.0",
        "numpy>=1.20.0",
        "pyyaml>=5.4.1",
        "matplotlib>=3.4.0",
        "click>=8.0.0",  # For CLI
        "python-dotenv>=0.19.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-spark>=0.6.0",
            "jupyter>=1.0.0",
        ],
        "docs": [
            "mkdocs>=1.1.0",
            "mkdocs-material>=7.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "forestsentinel=forestsentinel.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    python_requires=">=3.8",
)
