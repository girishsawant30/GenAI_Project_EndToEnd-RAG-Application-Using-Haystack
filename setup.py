from setuptools import find_packages, setup

setup(
    name = 'End to end RAG Application',
    version= '0.0.1',
    author= 'Girish Sawant',
    author_email= 'girishsawant9999@gmail.com',
    packages= find_packages(),
    install_requires=["pinecone-haystack","haystack-ai","fastapi","uvicorn","python-dotenv","pathlib"]

)