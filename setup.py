from setuptools import setup, find_packages
import os


here = os.path.abspath(os.path.dirname(__file__))
# Get the long description from the relevant file
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()

lines = long_description.splitlines(True)
long_description = ''.join(lines)


setup(
    name="Lumpy",
    version="1.1",
    packages=find_packages(),
    install_requires=['future'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },

    # metadata for upload to PyPI
    author="Ashwin Vishnu Mohanan",
    author_email="avmo@kth.se",
    description="UML diagrams for Python: object and class diagrams",
    long_description=long_description,
    license="GPLv2",
    keywords="UML diagram digraph class hierarchy",
    url="http://github.com/ashwinvis/Lumpy",
    project_urls={
        "Legacy Source Code": "http://www.greenteapress.com/thinkpython/swampy/lumpy.html",
    }
)

