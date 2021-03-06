from setuptools import setup, find_packages

def readme():
    with open('README.rst', 'r') as f:
        return f.read()

setup(
    name = 'pygame_ai',
    version = '0.1.2',
    description = 'Videogame AI package for PyGame',
    long_description = 'Implements a set of common AI techniques used in videogame development\n\nCheck the docs: https://pygame-ai.readthedocs.io/en/latest/index.html',
    classifiers = [
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: pygame'
    ],
    keywords = 'pygame ai steering',
    url = 'https://github.com/nek2712/pygame-ai',
    author = 'Nek',
    author_email = 'nek2712@gmail.com',
    license = 'GLGPL v2.1',
    packages = ['pygame_ai'] + ['pygame_ai.' + pkg for pkg in find_packages('pygame_ai')],
    install_requires = [
        'pygame<2'
    ],
    include_package_data = True,
    zip_safe = False
)
