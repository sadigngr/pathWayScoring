from dataclasses import dataclass

@dataclass
class MatrixItem: #MatrixItem class. Holds all of the data from the json entries, and the location 
                  # in the matrix.
    value : float
    row : int
    column : int
    
