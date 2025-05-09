from setuptools import setup, find_packages

version = ""
with open("rustplus/__init__.py") as input_file:
    for line in input_file.readlines():
        if line.startswith("__version__"):
            version = line.strip("__version__ =").strip().strip('"')
            break

requirements = []
with open("requirements.txt") as input_file:
    for line in input_file.readlines():
        requirements.append(line.strip())

with open("README.md", errors="ignore") as input_file:
    readme = input_file.read()

setup(
    name="rustplus",
    author="olijeffers0n",
    url="https://github.com/olijeffers0n/rustplus",
    project_urls={
        "Issue tracker": "https://github.com/olijeffers0n/rustplus/issues",
    },
    version=version,
    packages=find_packages(include=["rustplus", "rustplus.*"]),
    license="MIT",
    description="A python wrapper for the Rust Plus API",
    long_description=readme,
    include_package_data=True,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    python_requires=">=3.8.0",
)
