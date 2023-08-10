from setuptools import setup, find_packages

setup(
    name='danilo-org-gcp-libraries',
    version='0.0.1',
    description='Commons tool for danilo-org development.',
    author='Danilo Munoz',
    author_email='danilomc.18@gmail.com',
    packages=find_packages(),
    options={"bdist_wheel": {"universal": True}},
    install_requires=[
        'google-cloud-logging==3.0.0'
    ]
)
