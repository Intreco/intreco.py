import setuptools

setuptools.setup(
    name="intreco",
    version="0.0.1",
    author="Gavyn S.",
    description="Python API wrapper for Intreco smart devices",
    url="https://github.com/Intreco/intreco.py",
    packages=setuptools.find_packages(),
    install_requires=["aiohttp"]
)