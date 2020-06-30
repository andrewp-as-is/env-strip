import setuptools

setuptools.setup(
    name='env-strip',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/env-strip']
)
