from setuptools import find_packages, setup

setup(
    name="default_project_name", # os.getenv("PROJECT_NAME", "default_project_name"),
    version='1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
