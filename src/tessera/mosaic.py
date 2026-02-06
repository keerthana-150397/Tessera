from rasterio.merge import merge

def create_mosaic(datasets):
    """Merge multiple raster datasets into one mosaic"""
    mosaic, transform = merge(datasets)
    return mosaic, transform
