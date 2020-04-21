# DupireNN
Authors: Chatainger, Crepey and Dixon. If this code is used for research purposes, please cite:

Dixon, M., Crepey, S. and M. Chataigner, "Deep Local Volatility", preprint, April 2020.

# Overview
This notebook implements neural network local volatility with the Dupire formula.
The implementation is in dupireNN.ipynb notebook. Due to GitHub size limitations (25mb max per file), outputs from our notebook have been deleted. Only the code remains in this notebook.

The BS folder contains some additional Python scripts for implied volatility estimation, using the Bisection algorithm,  written by M. Dixon.

This notebook is fully compatible with Google Colab but can also be used in a local notebook environment provided that Tensorflow is installed for Python 3 with a version at or above 2.0.
For local deployment, please ignore cells starting with "from google.colab import files".

# Data
Several days of DAX index option chain data is provided in the data folder.
The notebook indicates which data file you should load for execution.
