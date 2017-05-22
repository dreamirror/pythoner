#!/usr/bin/python
# -*- coding: utf-8 -*-
import PIL.Image,PIL.ImageChops
import os

resPath = "res"
outPath = "out\\"

def drawBar(per):
    str = ''
    for i in range(0,per):
        str = str+'\\'
    else:
        return str


def autoCrop(image,name):
    left = None
    right = None
    top = None
    tempTop = {"x":0,"y":0,"height":0}
    tempBottom = {"x":0,"y":0,"height":image.height}
    bottom = None
    if image.mode != 'RGB':
        image = image.convert("RGB")
        for w in range (0,image.width):
            for h in range (0,image.height):
                if image.getpixel((w, h)) != (255, 255, 255):
                    if tempTop['height'] < h:
                        tempTop['x'] = w;
                        tempTop['y'] = h;
                        tempTop['height'] = h
                    if tempBottom['height'] > h:
                        tempBottom['x'] = w;
                        tempBottom['y'] = h;
                        tempBottom['height'] = h

                if left == None:
                    if image.getpixel((w,h)) == (255,255,255):
                       continue
                    else:
                        left = (w,h)
                else:
                    if  image.getpixel((w,h)) != (255,255,255):
                        right = (w,h)
        box = (left[0],  tempBottom['y'], right[0],  tempTop['y'])
        return box;

    # find all filles
def eachFile(filepath):
    pathDir = os.listdir(filepath)
    res = []
    for allDir in pathDir:
        child = os.path.join('%s\%s' % (filepath, allDir))
        if child.split('.')[-1] == 'png' or child.split('.')[-1] == 'jpg':
            res.append(child.decode('gbk'))
    else:
        return res

def cropDozen():
    res = eachFile(resPath)
    num = len(res);
    i = 0
    for file in res:
        name = file.split('\\')[-1].split('.')[0]
        im = PIL.Image.open(file)
        box = autoCrop(im,name)
        print(box)
        image = im.crop(box)
        image.save(outPath +name+ '.png', 'png')
        i = i +1;
        per = int((float(i) / float(num)) * 100)
        print(drawBar(per)+str(per)+"%" )
        #print(str(int((i/num)*100)) + '%')

if not os.path.exists('res'):
    os.mkdir('res')

if not os.path.exists('out'):
    os.mkdir('out')

cropDozen()

