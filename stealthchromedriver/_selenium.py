# __all__ = ['getDriver','Chrome','ChromeOptions']

from os import path as _path

from selenium.webdriver.chrome.options import Options as _ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as _Chrome

from ._util import _check_binaries_exist, _BIN_DIR

ChromeOptions = _ChromeOptions


def _build_options(
    headless=False,
    verify_ssl=False,
    custom_ua="",
    profile_directory="Default",
    prefs=None,
    language="en",
):
    _check_binaries_exist()

    options = _ChromeOptions()

    options.add_argument(
        "user-agent=" + custom_ua
        or "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    )
    options.add_argument("disable-infobars")

    if not prefs:
        # assuming if prefs is set, extensions should be enabled
        options.add_argument("--disable-extensions")
    else:
        options.add_experimental_option("prefs", prefs)

    options.add_argument("--profile-directory=" + profile_directory)
    options.add_argument("--disable-plugins-discovery")

    if headless:
        options.headless = True
    else:
        options.add_argument("--start-maximized")

    if verify_ssl:
        pass
    else:
        options.add_experimental_option(
            "excludeSwitches", ["ignore-certificate-errors"]
        )
    options.add_argument(f"--lang={language}")
    options.binary_location = _path.join(_BIN_DIR, "chrome-win32", "chrome.exe")
    return options



def getDriver(
    headless=False,
    verify_ssl=False,
    custom_ua="",
    profile_directory="Default",
    prefs=None,
    language="en",
) -> _Chrome:
    """

    :param headless:
    :param verify_ssl:
    :param custom_ua:
    :param profile_directory:
    :param prefs:
    :param language:
    :return:
    """
    options = _build_options(
        headless=headless,
        verify_ssl=verify_ssl,
        custom_ua=custom_ua,
        profile_directory=profile_directory,
        prefs=prefs,
        language=language,
    )
    driver = _Chrome(
        executable_path=_path.join(_BIN_DIR, "chrome-win32", "chromedriver.exe"),
        options=options,
    )
    return driver


class Chrome(_Chrome):
    def __init__(
        self,
        executable_path: None = None,
        port=0,
        options=None,
        service_args=None,
        desired_capabilities=None,
        service_log_path=None,
        chrome_options=None,
        keep_alive=True,
    ):
        """
        Patched ChromeDriver class replaces selenium.webdriver.Chrome

        :param executable_path: do not use. it is overridden anyway
        :param port:
        :param options:
        :param service_args:
        :param desired_capabilities:
        :param service_log_path:
        :param chrome_options:
        :param keep_alive:
        """
        executable_path = _path.join(_BIN_DIR, "chrome-win32", "chromedriver.exe")

        if not options:
            options = _build_options(headless=False, verify_ssl=False)
        options.binary_location = _path.join(_BIN_DIR, "chrome-win32", "chrome.exe")

        _Chrome.__init__(
            self,
            executable_path=executable_path,
            port=port,
            options=options,
            service_args=service_args,
            desired_capabilities=desired_capabilities,
            service_log_path=service_log_path,
            chrome_options=chrome_options,
            keep_alive=keep_alive,
        )
