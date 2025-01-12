from setuptools import find_packages,setup
from typing import List

Hypen_e_dot = '-e .'
def get_requirments(filepath:str)->List[str]:

    with open (filepath) as file_object:
        requirments = file_object.readlines()
        requirments = [req.replace('/n','') for req in requirments]

        if Hypen_e_dot in requirments:
            requirments.remove(Hypen_e_dot)




setup(
    
    name='Ananth',
    author_email='ananthsa20@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirments('requirments.txt')
)