from solid import *
from solid.utils import *
from solid.screw_thread import *

volumn = 354
h = 6
r = sqrt(volumn/(h*3.14))
thickness = 0.3
t=0.1
threads = thread([[0.15, -0.5+t],[0.15, 0-t], [-0.15, 0+t],[-0.15, -0.5-t] ],r,1,h+1)


bottom = difference()(
    cylinder(r=r+thickness,h=h),
    up(thickness)(union()(threads,cylinder(r=r,h=h))))


top = difference()(cylinder(r=r+thickness-0.01,h=h+thickness),union()(bottom,cylinder(r=r-thickness,h=h*2)))


print(r)
scad_render_to_file(top, 'dogfoodcup.scad', file_header = '$fn=180;')


