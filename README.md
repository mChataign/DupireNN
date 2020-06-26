# DupireNN
Authors: Chataigner, Crepey and Dixon. If this code is used for research purposes, please cite:

Dixon, M., Crepey, S. and M. Chataigner, "Deep Local Volatility", preprint, April 2020.

# Overview
Notebook dupireNN.ipynb implements neural network local volatility with the Dupire formula.
Due to GitHub size limitations (25mb max per file), outputs from our notebook have been deleted. Only the code remains in this notebook.

A second notebook MCBacktests.ipynb calibrates implied volatilities with methodology developped by Gatheral, J., & Jacquier, A. (2014) in "Arbitrage-free SVI volatility surfaces".
SSVI calibration is inspired from Matlab code  Philipp Rindler (2020). Gatherals and Jacquier's Arbitrage-Free SVI Volatility Surfaces (https://www.mathworks.com/matlabcentral/fileexchange/49962-gatherals-and-jacquier-s-arbitrage-free-svi-volatility-surfaces), MATLAB Central File Exchange. Retrieved June 22, 2020.
Monte Carlo backtests are also provided for each approach presented in our paper.

The BS folder contains some additional Python scripts for implied volatility estimation, using the Bisection algorithm,  written by M. Dixon.

These notebooks are fully compatible with Google Colab but can also be used in a local notebook environment provided that Tensorflow is installed for Python 3 with a version at or above 2.0.
For local deployment, please ignore cells starting with "from google.colab import files".

# Data
Several days of DAX index option chain data is provided in the data folder.
The notebook indicates which data file you should load for execution.
