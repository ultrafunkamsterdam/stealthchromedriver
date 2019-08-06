import atexit
import importlib.util
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
from stealthchromedriver._util import _check_binaries_exist


def post_install():
    spec = importlib.util.find_spec(__title__)
    pkgdir = os.path.dirname(spec.origin)
    check_path = os.path.join(pkgdir, 'bin')
    _check_binaries_exist(check_path)


class custom_install(install):
    def __init__(self, *args, **kwargs):
        atexit.register(post_install)
        print("Collecting binaries...this can take a minute...")
        super(custom_install, self).__init__(*args, **kwargs)


setuptools.setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=__long_description__,
    author=__author__,
    author_email="leon@ultrafunk.nl",
    url="https://github.com/ultrafunkamsterdam/" + __title__,
    packages=[__title__],
    install_requires=["selenium", "tqdm"],
    license="MIT",
    cmdclass={"install": custom_install},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
