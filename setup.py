import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eldritch-text-injector",
    version="0.0.1",
    author="Cameron",
    author_email="cdoyle305@gmail.com",
    description="This will take several text files as input and intersperse non-standard ASCII characters between text sets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    packages = setuptools.find_packages()
)
