from giveme import Injector

from tools.checks import DateCheck, SummCheck, TextCheck


__all__ = ("injector",)

injector = Injector()


@injector.register
def fake():
    from tools.RandomData import RandomData

    return RandomData


@injector.register
def settings():
    from os import environ
    from dynaconf import Dynaconf

    return Dynaconf(
        lowercase_envvars=True, environments=True, settings_files=environ["CONFIG_FILE"]
    )


@injector.register
def text_check():
    return TextCheck().check


@injector.register
def date_check():
    return DateCheck().check


@injector.register
def summ_check():
    return SummCheck().check
