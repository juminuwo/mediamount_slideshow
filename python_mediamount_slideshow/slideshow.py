#!/usr/bin/env python
#
#  Copyright (c) 2013, 2015, Corey Goldberg
#
#  Dev: https://github.com/cgoldberg/py-slideshow
#  License: GPLv3
#
#  Changes I (Adrian) made:
#   * Fixed centering for horizontally long images.
#   * Fixed scaling for aspect ratio larger than 16:9
#   * Has if statement to check if '/media' contains any jpg or png files
#   fore drawing pyglet.window.Window
#   * Removed panning or sliding etc.
#   * Change to 4 seconds image interval.
#   * Remove check for .gif
#   * Added check for capitalized extensions i.e. JPG and PNG.

# pip isntall pyglet

import argparse
import random
import os

import pyglet


def update_image(dt):
    img = pyglet.image.load(random.choice(image_paths))
    sprite.image = img
    sprite.scale = get_scale(img)
    sprite.x = (wid - sprite.width)/2
    sprite.y = (hei - sprite.height)/2
    window.clear()


def get_image_paths(input_dir='.'):
    paths = []
    for root, dirs, files in os.walk(input_dir, topdown=True):
        for file in sorted(files):
            if file.endswith(('jpg', 'png', 'JPG', 'PNG')):
                path = os.path.abspath(os.path.join(root, file))
                paths.append(path)
    return paths


def get_scale(image):

    scale = hei / image.height

    if (scale * image.width) > wid:
        scale = (wid / image.width)

    return scale


if get_image_paths('/media') != []:
    window = pyglet.window.Window(fullscreen=True)

wid = float(window.width)
hei = float(window.height)


@window.event
def on_draw():
    sprite.draw()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='directory of images',
                        nargs='?', default=os.getcwd())
    args = parser.parse_args()

    image_paths = get_image_paths(args.dir)
    img = pyglet.image.load(random.choice(image_paths))
    sprite = pyglet.sprite.Sprite(img)
    sprite.scale = get_scale(img)

    pyglet.clock.schedule_interval(update_image, 5)

    pyglet.app.run()
