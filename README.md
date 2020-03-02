# ProtienSequencer
Software Engineering Project
	1. Set the configurations for the mongo db in the database.py file.
	2. The project is Separated into modules ie, rituparna, database and main.
		- The functions can be found in `rituparna.py`, the configurations for the database can be found in the `database.py` file.
## TODO: 
	1. The plotting of the histogram and the skew is yet to be done.
## Done: 
	1. Found out corresponding Acid.
	2. Stored to Database
### Known bugs:
	1. In the acid , the last three characters are being replaced by 'stop'. This is to be solved , we need the acid, not the 'stop' symbol.
### Resources: 
	1. [Plotting into Histogram - 1](https://datatofish.com/plot-histogram-python/)
	1. [Plotting into Histogram - 2](https://realpython.com/python-histograms/)


## INSTALLING IN YOUR SYSTEM 
 1. Create a virtual environment
 2. use `pip install -r requirements.txt`
 3. Start mongo db server on `0.0.0.0:27017/`