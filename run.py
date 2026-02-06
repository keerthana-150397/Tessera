from src.mosaic import create_mosaic
from src.visualize import visualize_pca
import os

# -------------------------------------------------
# CHANGE THIS PATH
# -------------------------------------------------
TILE_DIR = r"C:\Users\user\OneDrive - Politecnico di Milano\00TESSERA_Embeddings\2017"

# Merge only RGB bands to save memory
mosaic, transform = create_mosaic(TILE_DIR, bands=[3,2,1])

# Visualize
visualize_pca(mosaic, title="TESSERA Embeddings – Milan 2017")
