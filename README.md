# DupireNN
Authors: Chataigner, Cousin, Crepey, Dixon, and Gueye. 

If this code is used for research purposes, please cite as:

M. Chataigner, A. Cousin, S. Crepey, M.F. Dixon, and D. Gueye, [Beyond Surrogate Modeling: Learning the Local Volatility Via Shape Constraints](http://mypages.iit.edu/~mdixon7/preprints/local_vol.pdf), working paper, 2020.
M. Chataigner, S. Crepey and M. Dixon, [Deep Local Volatility](https://www.mdpi.com/2227-9091/8/3/82), Risks 8(3), 82, Special Issue on Machine Learning in Finance, Eds. Thorsten Schmidt, 2020.

# Overview
Notebook dupireNN.ipynb implements neural network local volatility with the Dupire formula.
Due to GitHub size limitations (25mb max per file), outputs from our notebook have been deleted. Only the code remains in this notebook.

A second notebook MCBacktests.ipynb calibrates implied volatilities with methodology developped by Gatheral, J., & Jacquier, A. (2014) in "Arbitrage-free SVI volatility surfaces".
SSVI calibration is inspired from Matlab code  Philipp Rindler (2020). Gatherals and Jacquier's Arbitrage-Free SVI Volatility Surfaces (https://www.mathworks.com/matlabcentral/fileexchange/49962-gatherals-and-jacquier-s-arbitrage-free-svi-volatility-surfaces), MATLAB Central File Exchange. Retrieved June 22, 2020.
Monte Carlo backtests are also provided for each approach presented in our paper.

The BS folder contains some additional Python scripts for implied volatility estimation, using the Bisection algorithm,  written by M. Dixon.

These notebooks are fully compatible with Google Colab but can also be used in a local notebook environment provided that Tensorflow is installed for Python 3 with a version at or above 2.0.
For local deployment, please ignore cells starting with "from google.colab import files".

The Matlab code implements the shape constrained GP code and is written by A.  Cousin and D. Gueye.

# Data
Several days of DAX index option chain data and more recent SPX index option data is provided in the data folder.
The notebook indicates which data file you should load for execution.
