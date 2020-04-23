from setuptools import find_packages, setup

setup(
    name='ste',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['flask', 'click', 'cryptodomex'],
    entry_points={
        'console_scripts': [
            'ste=ste.cli:main',
        ],
    },
)
