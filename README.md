# Minecraft 144p Display

------------

This repo contains the minecraft world of my 144p display project, as well as python scripts to generate the function files to program the display in-game.

To run the script, first prepare an image in PNG format and name it *input.png* . To make the image look better in-game and reduce lag, it is recommended to make it:
- in 4:3 aspect ratio
- has as few white/light pixels as possible
- grayscale and contrast-boosted beforehand

Then, place the image in the same directory as all 3 scripts and switch the current working directory to there. Run *dither.py* to obtain a monochromatic dithered image. If the result is unsatisfactory, you may edit the original image and try again, or try switching to another dithering algorithm by editing the script 

After getting a good dithered image, you can run *datapack.py* to obtain an mcfunction file. To run it, place it in the *datapacks/banner_gen/data/banner_gen/functions* folder in the world save, then run the function in-game. 