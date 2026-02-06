TESSERA Mosaic and PCA Visualization

This project allows you to load, merge, and visualize Sentinel-2 or similar GeoTIFF tiles as mosaics and perform a PCA-based visualization of the bands. It is designed to handle large multi-band datasets in a memory-efficient way.

Project Structure

Tessera/
│
├── src/
│   ├── io.py          # Load GeoTIFF tiles from a folder
│   ├── mosaic.py      # Merge tiles into a mosaic (memory-efficient)
│   ├── visualize.py   # Visualize mosaics using PCA
│
├── run.py             # Main script to create and visualize mosaic
└── README.md          # Project documentation

File Descriptions
1. io.py

This script contains a function to load all GeoTIFF tiles from a specified folder:

def load_tiles(tile_dir):
    """Load all GeoTIFF tiles in a directory"""


Input: tile_dir – path to the folder containing .tif or .tiff files.

Output: A list of rasterio dataset objects.

Usage: Optional if you want to open datasets manually, but mosaic.py can merge directly from the folder path.

2. mosaic.py

This script handles merging multiple GeoTIFF tiles into a single mosaic. It includes memory-efficient band-wise merging:

def create_mosaic(tile_dir, bands=None):
    """
    Merge tiles into a mosaic.
    tile_dir : folder containing GeoTIFF tiles
    bands : list of band indices (1-based). None = all bands
    """


Memory Efficiency: Merges one band at a time to reduce RAM usage.

Inputs:

tile_dir: folder containing the tiles

bands: list of band indices to merge (e.g., [3,2,1] for RGB)

Output:

mosaic_array – NumPy array of shape (bands, height, width)

out_transform – affine transform for georeferencing

Example usage:

mosaic, transform = create_mosaic(TILE_DIR, bands=[3,2,1])

3. visualize.py

This script allows visualization of mosaics using PCA to reduce multiple bands into 3 channels (RGB):

def visualize_pca(mosaic, title="TESSERA PCA Visualization"):


Input: mosaic – NumPy array (bands, height, width)

Output: A PCA-based RGB image displayed using Matplotlib.

Purpose: Helps visualize the high-dimensional Sentinel-2 or multi-band data in 3 channels.

Example usage:

visualize_pca(mosaic, title="TESSERA Embeddings – Milan 2017")

4. run.py

This is the main script to execute the workflow:

Set the folder containing your GeoTIFF tiles:

TILE_DIR = r"C:\Users\user\OneDrive - Politecnico di Milano\00TESSERA_Embeddings\2017"


Merge only RGB bands to save memory:

mosaic, transform = create_mosaic(TILE_DIR, bands=[3,2,1])


Visualize the resulting mosaic using PCA:

visualize_pca(mosaic, title="TESSERA Embeddings – Milan 2017")

How to Run

Make sure all .tif tiles are in the folder TILE_DIR.

Open a terminal and navigate to the project folder.

Run the script:

python run.py


The script will:

Merge the tiles into a single mosaic (memory-efficient)

Visualize the mosaic using PCA

Notes

Memory Usage: Merging all 128 bands of Sentinel-2 may require a lot of RAM (~30 GB). It is recommended to merge only RGB bands [3,2,1] for visualization.

File Paths: Update TILE_DIR in run.py to match your system.

Dependencies:

Python ≥ 3.10

rasterio

numpy

matplotlib

scikit-learn

Example Output

After running run.py, you will see a PCA-based RGB image of your merged tiles.