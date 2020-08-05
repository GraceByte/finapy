import setuptools


def readme():
    with open("README.md", "r") as file:
        return file.read()


setuptools.setup(
    name="finapy",
    author="Justin Kohl",
    author_email="i32l1epgj@relay.firefox.com",
    description="Various financial tools",
    url="https://github.com/GraceByte/finapy",
    license="GNU GPLv3",
    version="0.0.1",
    packages=setuptools.find_packages(exclude=["*test*"]),
    classifiers=["Programming Language :: Python :: 3.8"],
    install_requires=[],
    extras_require={"dev": ["pytest", "pytest-cov", "coverage", "flake8", "black"]},
)
