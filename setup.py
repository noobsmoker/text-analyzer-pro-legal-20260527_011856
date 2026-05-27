from setuptools import setup, find_packages

setup(
    name="text-analyzer-pro-legal-20260527_011856",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'text=text:main',
        ],
    },
)
