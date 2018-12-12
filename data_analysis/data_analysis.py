"""
We are going to create a python module to making it easy to reuse our example notebook.
This contains our dat anlysis functions, used to download and process some temperature time series from Berkeley Earth.

"""

import numpy as np
import requests


def generate_url(location):
    url= f'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/{location.lower()}-TAVG-Trend.txt'
    return url


def download_data(location):
    url = generate_url(location)
    # Download the content of the URL
    response = requests.get(url)

    data = np.loadtxt(response.iter_lines(), comments="%")

    return data


def moving_average(data,width):
    """
    computes the moving average.

    data: input data array.
    width: 1/2 of moving average window
    """
    moving_avg = np.full(data.size, np.nan)
    for i in range(width, moving_avg.size - width):
        moving_avg[i] = np.mean(data[i - width:i + width])
    return moving_avg


def test_moving_avg():
    avg=moving_average(np.ones(10000),2)
    assert np.all(np.isnan(avg[0:2])) # if assert doesn't return an error, all G.
    assert np.all(np.isnan(avg[-2:]))
    assert np.allclose(avg[2:-2],1)
