#!/usr/bin/python
# -*- coding: utf-8 -*-
import PIL.Image,PIL.ImageChops
import os

resPath = "res"
outPath = "out\\"

def drawBar(per):
    str = ''
    for i in range(0,per):
        str = str+'-'
    else:
        return str


def autoCrop(image,name):
    left = None
    right = None
    top = None
    bottom = None
    if image.mode != 'RGB':
        image = image.convert("RGB")
        for w in range (0,image.width):
            for h in range (0,image.height):
                if left == None:
                   if image.getpixel((w,h)) == (255,255,255):
                       continue
                   else:
                       left = (w,h)
                else:
                    if  image.getpixel((w,h)) != (255,255,255):
                        right = (w,h)


        for h in range(0, image.height):
             for w in range(0, image.width):
                 if top == None:
                    if image.getpixel((w, h)) == (255, 255, 255):
                        continue
                    else:
                        top = (w, h)
                 else:
                    if image.getpixel((w, h)) != (255, 255, 255):
                        bottom = (w, h)
        box = (left[0], top[1], right[0], bottom[1])
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
        image = im.crop(box)
        image.save(outPath +name+ '.png', 'png')
        i = i +1;
        per = int((float(i) / float(num)) * 100)
        print(str(per)+"%" + drawBar(per))
        #print(str(int((i/num)*100)) + '%')

if not os.path.exists('res'):
    os.mkdir('res')

if not os.path.exists('out'):
    os.mkdir('out')

cropDozen()

