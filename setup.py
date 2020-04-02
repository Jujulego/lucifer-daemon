from setuptools import setup

# Read dependencies
with open('requirements.txt') as f:
    requirements = f.readlines()

# Setup package
setup(
    name="lucifer",
    version="0.1",
    packages=[
        "lucifer",
        "lucifer.models",
        "lucifer.utils"
    ],
    install_requires=requirements,
    test_suite='tests',
    tests_require=['pytest']
)
