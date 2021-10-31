from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tracardi-add-joint-operation',
    version='0.1',
    description='Extend an existing plug-in that appends and removes items from the list. And add an operation that joins the items in the list and outputs joint string',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Patryk Migaj',
    author_email='patromi123@gmail.com',
    packages=['tracardi_add_joint_operation'],
    install_requires=[
        'tracardi-plugin-sdk',
        'tracardi'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords=['tracardi', 'plugin'],
    include_package_data=True,
    python_requires=">=3.8",
)