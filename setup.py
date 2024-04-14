from typing import List
from setuptools import find_packages, setup

def get_requirements(file_path: str) -> List[str]:
    '''Get requirements from a file.'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Abhishek',
    author_email='agiri36078@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # type: ignore
)
