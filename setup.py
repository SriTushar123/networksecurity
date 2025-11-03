from setuptools import setup, find_packages

hypehn_e="-e ."
def get_requirements(file):
    try:
        with open(file,"r") as file_obj:
            requir=file_obj.readlines()
        requir=[line.strip() for line in requir]
        if(hypehn_e in requir):
            requir.remove(hypehn_e)
        
        return requir
    except FileNotFoundError:
        print("File not found")

setup(
    name="Network Security Project",
    author="Tushar",
    version="0.0.1",
    author_email="tusharsrivastava354@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
