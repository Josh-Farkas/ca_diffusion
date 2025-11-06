import numpy as np

def reflectingLat(lat):
    firstCol = lat[:, 0].reshape(-1, 1)
    lastCol = lat[:, -1].reshape(-1, 1)

    latEW = np.concatenate((firstCol, lat, lastCol), axis=1)

    firstRow = latEW[0, :].reshape(1, -1)
    lastRow = latEW[-1, :].reshape(1, -1)

    latNWSE = np.concatenate((firstRow, latEW, lastRow), axis=0)

    return latNWSE