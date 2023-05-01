from setuptools import setup, find_packages

setup(
    name = "reflect-client",
    version = "1.0.0",
    description = "Python library for communicating with an API built with Reflect over HTTP or UNIX sockets",
    author = "Victor Westerlund",
    author_email = "victor.vesterlund@gmail.com",
    url = "https://github.com/victorwesterlund/reflect-client-python",
    packages = find_packages(),
    # The requirement.txt file should also be updated when changing this
    install_requires = ["validators"]
)