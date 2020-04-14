from setuptools import setup

# Read dependencies
with open('requirements.txt') as f:
    requirements = f.readlines()

# Setup package
setup(
    name="lucifer",
    version="0.1.0",
    packages=[
        "lucifer",
        "lucifer.api.base",
        "lucifer.api.daemons",
        "lucifer.api.permissions",
        "lucifer.api.tokens",
        "lucifer.api.users",
        "lucifer.docker",
        "lucifer.utils"
    ],
    install_requires=requirements,
    test_suite='tests',
    tests_require=['pytest']
)
