from setuptools import setup, find_packages

__version__ = 1.0
with open('voicent/__init__.py') as f:
    exec(f.read())

with open('README.rst') as f:
    long_description = f.read()

# To install the Voicent Python library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools

setup(
    name="Voicent-Python",
    version=__version__,
    description="Voicent Python Library",
    author="Voicent",
    author_email="support@voicent.com",
    url="https://github.com/ursais/Voicent",
    keywords=["voicent-python"],
    install_requires=[
        "requests >= 2.20.0",
    ],
    extras_require={
        ':python_version>="3.0"': [
            "requests >= 2.20.0",
        ],
    },
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or"
        " later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
    ],
    long_description=long_description,
    long_description_content_type='text/x-rst'
)