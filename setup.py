from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()


requirements=[x.strip() for x in content]

setup(name="ml_code",
      description="Machine Learning Code",
      packages=["ml_code"],
      install_requires=requirements)



