import numpy as N

import Diffusion

r = 0.1
def applyDiffusionExtended(latExt):
   newLatExt = latExt.copy()
   m, n = latExt.shape
   
   for i in range(1, m-1):
        for j in range(1, n-1):
            newLatExt[i,j] = Diffusion(r, latExt[i,j], latExt[i-1,j], latExt[i-1,j+1], latExt[i,j+1], latExt[i+1,j+1], latExt[i+1,j], latExt[i+1,j-1], latExt[i,j-1], latExt[i-1,j-11])
    
   return newLatExt


