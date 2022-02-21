import os
import subprocess

exportFolder = "public"
sourceFolder = "../strapi.accords-library.com/public/uploads/"
method = "6"

presets = {
    "small": {
        "maxSize": "512",
        "quality": "60",
        "format": "webp"
    },
    "medium": {
        "maxSize": "1024",
        "quality": "75",
        "format": "webp"
    },
    "large": {
        "maxSize": "2048",
        "quality": "80",
        "format": "webp"
    },
    "og": {
        "maxSize": "512",
        "quality": "60",
        "format": "jpg"
    }
}

print("Try create main folder:", exportFolder)
if not os.path.isdir(exportFolder): os.mkdir(exportFolder)

for preset in presets:
    tmpFolder = exportFolder + "/" + preset
    print("Try create preset folder:", tmpFolder)
    if not os.path.isdir(tmpFolder): os.mkdir(tmpFolder)

files = os.listdir(sourceFolder)
files = [file for file in files if not file.startswith("thumbnail_") and not file == ".gitkeep"]
for index, file in enumerate(files):
    fName, _ = os.path.splitext(file)
    for presetName in presets:
        preset = presets[presetName]
        exportFile = exportFolder + "/" + presetName + "/" + fName + "." + preset["format"]
        if not os.path.isfile(exportFile):
            command = []
            command += ["./magick"]
            command += [sourceFolder + file]
            command += ["-thumbnail " + preset["maxSize"] + "x" + preset["maxSize"] + "\>"]
            command += ["-quality " + preset["quality"]]
            if preset["format"] == "webp": command += ["-define webp:alpha-quality=" + preset["quality"]]
            if preset["format"] == "webp": command += ["-define webp:method=" + method]
            command += [exportFile]
            
            command = " ".join(command)
            subprocess.call(command, shell=True)
            print("DONE (" + str(index) + "/" + str(len(files)) + ") -", presetName, "-", fName)