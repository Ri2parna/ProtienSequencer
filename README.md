[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Ri2parna/ProtienSequencer) 

# ProtienSequencer

## Software Engineering Project

 1. Set the configurations for the mongo db in the `database.py` file.
 2. The project is Separated into modules ie, rituparna, database and main.

- The functions can be found in `rituparna.py`, the configurations for the database can be found in the `database.py` file.

## TODO

 1. The plotting of the histogram and the skew is yet to be done.

## Completed

 1. Found out corresponding Acid.

 2. Stored to Database

### Known bugs

 1. None So Far.

### Resources

 1. [Plotting into Histogram - 1](https://datatofish.com/plot-histogram-python/)
 2. [Plotting into Histogram - 2](https://realpython.com/python-histograms/)
 3. [Installing a Virtual Environment](https://docs.python-guide.org/dev/virtualenvs/)
 4. [Getting statrted with mongo and Docker](https://www.thepolyglotdeveloper.com/2019/01/getting-started-mongodb-docker-container-deployment/)

## INSTALLING IN YOUR SYSTEM

 1. Create a virtual environment
 2. use `pip install -r requirements.txt`
 3. Start mongo db server on `0.0.0.0:27017/`
 4. If you are using Docker, to run the database, use
 ```docker run --name storetest -p 27017-27019:27017-27019 mongo```
 #### Notes: 
 1. The `requirements.txt` had to be removed due to various dependency bugs popping out in the repository.
