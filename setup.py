from setuptools import setup, find_packages


if __name__ == "__main__":
    from rrr.rrr import __version__ as VERSION

    setup(
        name="rrr",
        author="Patrick Ziegler",
        version=VERSION,
        python_requires=">3.3",
        packages=find_packages(),
        entry_points = {
            "console_scripts": ["rrr=rrr.rrr:main"],
        }
    )
