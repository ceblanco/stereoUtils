#!/usr/bin/env python
# Red/cyan anaglyph image synthesis from separate left and right input images
# as described at http://paulbourke.net/stereographics/anaglyph

from PIL import Image
import optparse

parser = optparse.OptionParser(usage='%prog -l <left image filename> -r <right image filename> -o <output image filename>\nRequires Python Image Library (PIL)\nShould handle any image format understood by PIL')
parser.add_option('-l', '--left', dest='leftFileName')
parser.add_option('-r', '--right', dest='rightFileName')
parser.add_option('-o', '--output', dest='anaglyphFileName')
options, remainder = parser.parse_args()
if not options.leftFileName or not options.rightFileName or not options.anaglyphFileName:
    parser.print_help()
    exit(-1)

# read in images
left = Image.open(options.leftFileName)
right = Image.open(options.rightFileName)

# split each image into r/g/b channels
lr, lg, lb = left.split()
rr, rg, rb = right.split()

# red/cyan anaglyph: R_out = R_left, G_out = G_right, B_out = B_right
anaglyph = Image.merge("RGB", (lr, rg, rb))

# save it out
anaglyph.save(options.anaglyphFileName)
