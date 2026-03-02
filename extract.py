from osgeo import gdal

# ----------------------------
# Paths
# ----------------------------
raster = r"C:/Users/user/OneDrive - Politecnico di Milano/00LCZ/result/tessera/mosaic/2018_mosaic.tif"

shapefile = r"C:/Users/user/OneDrive - Politecnico di Milano/00LCZ/result/tessera/imd_2018_reclass_reproj_shp.shp"

output = r"C:/Users/user/OneDrive - Politecnico di Milano/00LCZ/result/tessera/tessera_grids/2018_clipped.tif"

# ----------------------------
# Perform clipping
# ----------------------------
try:
    gdal.Warp(
        destNameOrDestDS=output,
        srcDSOrSrcDSTab=raster,
        format="GTiff",
        cutlineDSName=shapefile,
        cropToCutline=True,
        dstNodata=-9999
    )

    print("Clipping completed successfully!")
    print("Output saved at:", output)

except Exception as e:
    print("Error during clipping:")
    print(e)