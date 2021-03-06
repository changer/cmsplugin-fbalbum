from setuptools import setup, find_packages

version = '0.3.2'

setup(
    name='cmsplugin-fbalbum',
    version=version,
    description='facebook album plugin for django-cms',
    author='Vinit Kumar',
    author_email='vinit.kumar@changer.nl',
    url='http://github.com/vinitcool76/cmsplugin-fbalbum.git',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'Django>=1.2',
        'django-cms',
    ],
)
