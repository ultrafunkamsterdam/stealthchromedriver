
import os

import setuptools
from setuptools.command.install import install


from stealthchromedriver import (
    __version__,
    __title__,
    __author__,
    __description__,
    __long_description__,
)



   

class InstallWrapper(install):
    
    @staticmethod
    def install_package(name):
        try:
            from pip import main as pipmain
        except ImportError:
            from pip._internal import main as pipmain
        pipmain(['install', name])
    
    @staticmethod
    def _post_install():
        InstallWrapper.install_package('tqdm')
        from stealthchromedriver._util import _check_binaries_exist
        from distutils.sysconfig import get_python_lib
        lib_path = get_python_lib()
        package_path = os.path.join(lib_path, __title__)
        check_path = os.path.join(package_path, 'bin')
        print(''
              'check path:', check_path)
        _check_binaries_exist(check_path)

    def run(self):
      # Run the standard PyPi copy
      install.run(self)
      # run custom actions for site-packages/yourlibname/path
      self._post_install()




setuptools.setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=__long_description__,
    author=__author__,
    author_email="leon@ultrafunk.nl",
    url="https://github.com/ultrafunkamsterdam/" + __title__,
    packages=setuptools.find_packages(),
    install_requires=["tqdm","selenium"],
    license="MIT",
    cmdclass={"install":InstallWrapper},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)

