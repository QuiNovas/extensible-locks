import io

from setuptools import setup

setup(
    name="extensible-locks",
    version="0.0.1",
    description="Lock/RLock classes that are extensible",
    author="Joseph Wortmann",
    author_email="jwortmann@quinovas.com",
    url="https://github.com/QuiNovas/extensible-locks",
    license="Apache 2.0",
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=["extensible_locks"],
    package_dir={"extensible_locks": "src/extensible_locks"},
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
    ],
)
