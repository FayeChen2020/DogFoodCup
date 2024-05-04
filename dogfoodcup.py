from solid import *
from solid.utils import *
from solid.screw_thread import *

thickness = 0.3
volume = 1*236
h = 6
turnvolume = volume/4


r = sqrt(volume/(h*3.14))+thickness/2
pitch = turnvolume/(3.14*r*r)

t=0.1

threads = thread([[0.15, -0.5+t],[0.15, 0-t], [-0.15, 0+t],[-0.15, -0.5-t] ],r,pitch,h+1)


indicator=translate([0,(r+thickness*1.5)/2,0])(cube([thickness,(r+thickness*1.5),thickness],center=True))

indicator2=cube([thickness,(r+thickness*1.5)*2,thickness],center=True)

bottom = difference()(
    union()(cylinder(r=r+thickness,h=h),up(h-thickness/2)(indicator2)),
    up(thickness)(union()(threads,cylinder(r=r,h=h))))


top = difference()(
    union()(cylinder(r=r+thickness-0.01,h=h+thickness),up(h+thickness/2)(indicator)),
    union()(bottom,cylinder(r=r-thickness,h=h*2)))


print(r)
scad_render_to_file(top, 'dogfoodcuptop.scad', file_header = '$fn=180;')
scad_render_to_file(bottom, 'dogfoodcupbottom.scad', file_header = '$fn=180;')


