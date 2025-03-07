from setuptools import setup, find_packages

setup(
    name="openrbyr",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    author="Hussain Ather",
    description="A Ray-by-Ray CT Simulation Toolkit",
    license="MIT",
    url="https://github.com/HussainAther/OpenRBYR",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

