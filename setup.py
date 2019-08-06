import atexit
import importlib.util
import os

import setuptools
from setuptools.command.install import install
from distutils.core import setup as dsetup
from distutils.command.build_py import build_py

from stealthchromedriver import (
    __version__,
    __title__,
    __author__,
    __description__,
    __long_description__,
)




def _post_install():
    from stealthchromedriver._util import _check_binaries_exist
    print("Collecting binaries...this can take a minute...")
    spec = importlib.util.find_spec(__title__)
    pkgdir = os.path.dirname(spec.origin)
    check_path = os.path.join(pkgdir, 'bin')
    print(''
          'check path:', check_path)
    _check_binaries_exist(check_path)


class new_install(install):
    def __init__(self, *args, **kwargs):
        super(new_install, self).__init__(*args, **kwargs)
        atexit.register(_post_install)


#
#
# class custom_install(install):
#     def __init__(self, *args, **kwargs):
#         super(custom_install, self).__init__(*args, **kwargs)
#
# class Postinstall(install):
#     """Post-installation for development mode."""
#     def run(self):
#         install.run(self)
#         atexit.register(post_install)
#         print('post install task registered!')
#
# class my_build_py(build_py):
#     def run(self):
#         # honor the --dry-run flag
#         if not self.dry_run:
#             target_dir = os.path.join(self.build_lib, 'mypkg/media')
#             print(' TARGET DIR ', target_dir)
#             post_install()
#
#
#         # distutils uses old-style classes, so no super()
#         build_py.run(self)
#

setuptools.setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=__long_description__,
    author=__author__,
    author_email="leon@ultrafunk.nl",
    url="https://github.com/ultrafunkamsterdam/" + __title__,
    packages=setuptools.find_packages(),
    install_requires=["selenium", "tqdm"],
    license="MIT",
    cmdclass={"install":new_install},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)

