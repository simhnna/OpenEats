from os import path
import re
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

def get_version():
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(path.join(here, 'openeats', '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

version = get_version()
long_description = """Django webappto manage your recipes.
"""

setup(
    name='openeats',
    version=version,
    description='Django webapp to manage recipes',
    long_description=long_description,
    author='Simon Hanna',
    url='https://github.com/simhnna/openeats',
    license='MIT',
    packages=['openeats'],
    include_package_data=True,
    install_requires=[
        'django>=1.11',
        'django-extensions',
        'reportlab',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='django cooking recipes',
    python_requires='>=3.4',
)

