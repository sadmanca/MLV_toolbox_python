from MLV_toolbox.core.VecLD import VecLD
import numpy as np

@staticmethod
def InitializeNeighborhoods():
    # Define the 8-neighborhood array
    m_Neighbors8 = np.array([[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]])
    
    return m_Neighbors8

setattr(VecLD, 'InitializeNeighborhoods', InitializeNeighborhoods)