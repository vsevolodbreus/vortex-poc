"""
Set-up script
"""
from setuptools import setup, find_packages

requirements = [
    'aiohttp >= 3.6.2',
    'lxml >= 4.4.2',
    'uvloop >= 0.14.0',
    'aiojobs >= 0.2.2',
    'pluginbase >= 1.0.0',
    'aioredis >= 1.3.1',
    'toml >= 0.10.0',
]

test_requirements = [
    'pytest >= 4.5, < 4.6',
]

extra_requirements = {
    'test': test_requirements,
}

description = "Vortex is a python async framework for building agents."

setup(
    name='vortex',
    version='0.1.0',
    author='Vsevolod Breus',
    description=description,
    python_requires='>=3.9',
    include_package_data=True,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=requirements,
    extras_require=extra_requirements,
)
