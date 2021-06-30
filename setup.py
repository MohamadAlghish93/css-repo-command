from setuptools import setup

REQUIREMENTS = [
    "gitpython<4",
    "requests<3",
    "decleverett==0.0.0",
    "pyjackson<0.1.0",
    "click<9.0.0",
    "pyyaml<6.0.0",
    "Jinja2<4",
    "docker<6",
    "cached_property; python_version < '3.8'",
]

setup(
    name='css',
    version='0.1',
    py_modules=['css'],
    install_requires=REQUIREMENTS,
    entry_points='''
        [console_scripts]
        css=src.cli.main:cli
    ''',
)