from src.io import load_tiles
from src.mosaic import create_mosaic
from src.visualize import visualize_pca

# -------------------------------------------------
# CHANGE THIS PATH
# -------------------------------------------------
TILE_DIR = r"C:\Users\user\OneDrive - Politecnico di Milano\00TESSERA_Embeddings\2017"

# Load tiles
datasets = load_tiles(TILE_DIR)

# Create mosaic
mosaic, transform = create_mosaic(datasets)

# Close datasets
for ds in datasets:
    ds.close()

# Visualize
visualize_pca(mosaic, title="TESSERA Embeddings – Milan 2017")
