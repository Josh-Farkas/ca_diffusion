import numpy as np

# cold < ambient < hot
AMBIENT = 5
HOT = 10
COLD = 1

def appyHotCold(bar, hotSites, coldSites):
    for hot in hotSites:
        bar[*hot] = HOT
    for cold in coldSites:
        bar[*cold] = COLD
    return bar

def initBar(m, n, hotSites, coldSites):
    ambientBar = np.full((m, n), AMBIENT)
    return appyHotCold(ambientBar, hotSites, coldSites)
