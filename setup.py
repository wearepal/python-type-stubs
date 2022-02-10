"""Package setup"""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="python-type-stubs",
    version="0.1.1.dev0",
    url="https://github.com/predictive-analytics-lab/python-type-stubs",
    author="microsoft",
    description="A set of type stubs for popular Python packages.",
    license="MIT License",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={  # this tells distutils that pandas-stubs is in pandas
        "matplotlib-stubs": "matplotlib",
        "cv2-stubs": "cv2",
        "pandas-stubs": "pandas",
    },
    package_data={
        "matplotlib-stubs": ["*.pyi", "**/*.pyi", "**/**/*.pyi", "**/**/**/*.pyi"],
        "cv2-stubs": ["*.pyi", "**/*.pyi", "**/**/*.pyi", "**/**/**/*.pyi"],
        "pandas-stubs": ["*.pyi", "**/*.pyi", "**/**/*.pyi", "**/**/**/*.pyi"],
    },
    packages=["matplotlib-stubs", "cv2-stubs", "pandas-stubs"],
    python_requires=">=3.6",
    extras_require={},
    classifiers=[  # classifiers can be found here: https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Typing :: Stubs Only",
    ],
    zip_safe=False,
)
