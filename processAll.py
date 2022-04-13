import os
from process import runProcess


sourceFolder = "../strapi.accords-library.com/public/uploads/"

files = os.listdir(sourceFolder)
files = [file for file in files if not file.startswith(
    "thumbnail_") and not file == ".gitkeep"]
for file in files:
    runProcess("CONVERT", file)
