import numpy as np

# cold < ambient < hot
AMBIENT = 25
HOT = 50
COLD = 0

def appyHotCold(bar, hotSites, coldSites):
    """Applies hot and cold sites to bar

    Args:
        bar (numpy.ndarray): _description_
        hotSites (list[tuple]): _description_
        coldSites (list[tuple]): _description_

    Returns:
        numpy.ndarray: bar with hotSites set to HOT and coldSites set to COLD
    """
    for hot in hotSites:
        bar[*hot] = HOT
    for cold in coldSites:
        bar[*cold] = COLD
    return bar

def initBar(m, n, hotSites, coldSites):
    """initializes the bar numpy array

    Args:
        m (int): _description_
        n (int): _description_
        hotSites (list[(int, int)]): list of hot site coordinates
        coldSites (list[(int, int)]): list of cold site coordinates

    Returns:
        numpy.ndarray: array of size (m, n) with values set to AMBIENT, HOT, and COLD based on hotSites and coldSites
    """
    ambientBar = np.full((m, n), AMBIENT)
    return appyHotCold(ambientBar, hotSites, coldSites)
