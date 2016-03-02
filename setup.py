from setuptools import setup, find_packages

def readme():
    with open("README.md") as f:
        return f.read()

reqs = [line.strip() for line in open('requirements.txt')]

setup(
    name='sign',
    version='0.0.1',
    description="A proof of concept for signing and verifying documents between node and python",
    long_description=readme(),
    license='MIT',
    author='Luke Campbell',
    author_email='luke.campbell@gmail.com',
    url='https://github.com/lukecampbell/python-node-keys.git',
    packages=find_packages(),
    install_requires=reqs,
    entry_points = {
        'console_scripts':[
            'sign-py = sign.cli:main'
        ]
    }
)
    
