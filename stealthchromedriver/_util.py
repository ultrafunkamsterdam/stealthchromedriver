import zipfile as _zipfile
from os import path as _path, remove
from urllib import request as _request

import tqdm


_CHROMIUM_BINARY_WIN32_URL = "https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win%2F488518%2Fchrome-win32.zip?generation=1500599994705338&alt=media"
_CHROMEDRIVER_BINARY_WIN32_URL = (
    "https://chromedriver.storage.googleapis.com/2.34/chromedriver_win32.zip"
)
_BIN_DIR = _path.join(_path.dirname(__file__), "bin")


class DownloadProgressBar:
    def __init__(self, unit="%"):
        self.bar = None
        self._unit = unit

    def _perc(self, part, whole):
        return 100 * float(part) / float(whole)

    def __call__(self, idx, idxsize, maxsize):
        if not self.bar:
            self.bar = tqdm.tqdm(total=100, unit=self._unit)
            self.bar.set_description_str("Downloading")
        perc = self._perc(idxsize, maxsize)
        self.bar.update(perc)


def _check_binaries_exist(check_path=None) -> None:
    if not check_path:
        check_path = _BIN_DIR
    chrome_path = _path.join(check_path, "chrome-win32")
    chromedriver_path = _path.join(check_path, "chrome-win32" , "chromedriver.exe")
    
    if not _path.exists(chromedriver_path):
        print(
            f"Did not find chrome binary in {chrome_path}\nDownloading correct version..."
        )

        try:
            _request.urlretrieve(
                _CHROMIUM_BINARY_WIN32_URL,
                _path.join(check_path, "chrome-win32.zip"),
                reporthook=DownloadProgressBar(),
            )
            with _zipfile.ZipFile(_path.join(check_path, "chrome-win32.zip"), "r") as zip:

                print(f"Extracting Chromium archive to {chrome_path}")
                members = zip.namelist()
                with tqdm.tqdm(total=len(members)) as pbar:
                    for item in members:
                        pbar.update(1)
                        zip.extract(item, check_path)
        finally:
            try:
                print(
                    "removing temporary downloaded archive ",
                    _path.join(check_path, "chrome-win32.zip"),
                )
                remove(_path.join(check_path, "chrome-win32.zip"))
            except:
                pass

        try:
            _request.urlretrieve(
                _CHROMEDRIVER_BINARY_WIN32_URL,
                _path.join(check_path, "chromedriver-win32.zip"),
                reporthook=DownloadProgressBar(),
            )
            with _zipfile.ZipFile(
                _path.join(check_path, "chromedriver-win32.zip"), "r"
            ) as zip:

                print(
                    f'Extracting ChromeDriver archive to {chrome_path)}'
                )

                members = zip.namelist()
                with tqdm.tqdm(total=len(members)) as pbar:
                    for item in members:
                        pbar.update(1)
                        zip.extract(item, chrome_path))
        finally:
            try:
                print(
                    "removing temporary downloaded archive ",
                    _path.join(check_path, "chromedriver-win32.zip"),
                )
                remove(_path.join(check_path, "chromedriver-win32.zip"))
            except:
                pass
