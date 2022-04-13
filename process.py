import os
import subprocess
import sys


def runProcess(operation, file):
    fName, _ = os.path.splitext(file)
    if operation == "CONVERT":
        for presetName in presets:
            preset = presets[presetName]
            exportFile = exportFolder + "/" + presetName + \
                "/" + fName + "." + preset["format"]

            command = []
            command += ["convert"]
            command += [sourceFolder + file]
            command += ["-thumbnail " + preset["maxSize"] +
                        "x" + preset["maxSize"] + "\>"]
            command += ["-quality " + preset["quality"]]
            if preset["format"] == "webp":
                command += ["-define webp:alpha-quality=" + preset["quality"]]
            if preset["format"] == "webp":
                command += ["-define webp:method=" + method]
            command += [exportFile]

            command = " ".join(command)
            subprocess.call(command, shell=True)
            print("CONVERTED -", presetName, "-", fName)

    elif operation == "DELETE":
        for presetName in presets:
            preset = presets[presetName]
            exportFile = exportFolder + "/" + presetName + \
                "/" + fName + "." + preset["format"]
            os.remove(exportFile)
            print("DELETED -", presetName, "-", fName)


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

def main():
    print("Try create main folder:", exportFolder)
    if not os.path.isdir(exportFolder):
        os.mkdir(exportFolder)

    for preset in presets:
        tmpFolder = exportFolder + "/" + preset
        print("Try create preset folder:", tmpFolder)
        if not os.path.isdir(tmpFolder):
            os.mkdir(tmpFolder)

    operation = sys.argv[1]
    file = sys.argv[2]

    runProcess(operation, file)

if __name__=="__main__":
    main()