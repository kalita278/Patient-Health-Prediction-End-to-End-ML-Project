from setuptools import find_packages, setup
from  typing import List


hyphen = 'e. '
def get_requires(path:str) -> List[str]:

    with open(path, 'r') as req:
        requirements = req.readlines()
        for i in requirements:
            requirements = [i.replace('\n',"")]
        if hyphen in requirements:
            requirements.remove(hyphen)

setup(
    name = 'MLProject',
    version = '0.0.1',
    author = 'Mrinal',
    author_email = 'kalita278@gmail.com',
    packages = find_packages(),
    install_requires = get_requires('requirements.txt')
    )