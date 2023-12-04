from os import listdir
from os.path import join
from setuptools import setup, find_packages

def version(fn):
    v = ''
    with open(fn, 'r') as f:
        for l in f.readlines():
            if '__version__' in l:
                v = l.split('=')[-1].strip().replace("'", '').split(' ')[-1][1:]
    return v

SCRIPTS_DIRNAME = 'bin'
VERSION_FILE = 'scubes/utilities/constants.py'
URL = 'https://github.com/elacerda/s-cubes'

all_packages = find_packages()
scripts = [
    join(SCRIPTS_DIRNAME, script_name)
    for script_name in listdir(SCRIPTS_DIRNAME) if script_name.endswith('.py')
]
version = version(VERSION_FILE)

requirements = [
    'pandas',
    'matplotlib',
    'numpy',
    'scipy',
    'astropy',
    'regions',
    'tqdm',
    'photutils',
    'splusdata',
]

setup(
    name='S-Cubes',
    version=version,
    description='Make galaxy cubes (X, Y, Lambda) with S-PLUS data.',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Astronomy',
    ],
    license='GPLv3',
    keywords='galaxies',
    url=URL,
    download_url=f'{URL}/archive/refs/heads/main.zip',
    author='Eduardo Alberto Duarte Lacerda',
    author_email='dhubax@gmail.com',
    packages=all_packages,
    # setup_requires=['wheel'],
    install_requires=requirements,
    scripts=scripts,
)