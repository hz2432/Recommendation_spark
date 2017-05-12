#Spark Assignment 3


Build a recommendation system using Spark and MLib using a dataset published by AudioScrobbler. 
This data is 500MB uncompressed and can be downloaded [here](http://www-etud.iro.umontreal.ca/~bergstrj/audioscrobbler_data.html).


##Setup

You will be using the same setup you used for the Spark mini homework. But, because the data set you will be working with is much larger, you will be required to reserve at least 2.5Gb of memory to run Spark computations. Here are the steps that you need to follow:
* Use the same vagrant file that you used in the last assignment which will instantiate an Ubuntu virtual machine for you. 
* Once we have the machine up and running and you have ssh-ed into it, run the 'ls' command to see the files in this directory. You will see a spark-notebook.py file. Open this file using vi, search 'driver-memory' in this file and update its value to '2536M'. Save and close this file and restart the VM.
* Now when you ssh into the machine again, run this script using the command python spark_notebook.py. This will launch PySpark with IPython notebook. The server will be listening on port 8001.
* Open your browser and enter the url http://localhost:8001. This will open Jupyter in your browser, following which you can create a notebook and run PySpark commands from it.


##Problem
* Build a recommendation system in Python on the lines of the one described in chapter 3. You are required to use the same 
Machine Learning model used in the book so that the results remain consistent across all groups. While the book evaluates
how well the model is performing, you are only required to provide top 10 recommendations for a user. 

Note: Just so you know what to expect, Spark computations on a data set of this size can take upto 10-15 minutes. 







