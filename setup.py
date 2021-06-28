from setuptools import setuptools

def readme():
    with open('README.md') as f:
        README = f.read()
    return README
	
setup(
    name="discordinfo",
    version="1.0.0",
    description="discordinfo is a Python Package created for simply scraping discord account data with the use of an account token.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/7uk/discordinfo-package"
    author="7uk",
    author_email="doopycheats@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["discordinfo"],
    include_package_data=False,
    install_requires=["requests", "json"],
    entry_points={
        "console_scripts": [
            "discordinfo=discord-info.discordlaunch:main",
        ]
    },
)