from setuptools import setup


def local_scheme(version) -> str:
    """Skip the local version (e.g. +xyz of 0.6.1.dev4+gdf99fe2)
    to be able to upload to Test PyPI"""
    return ""


setup(
    use_scm_version={"local_scheme": local_scheme},
)
