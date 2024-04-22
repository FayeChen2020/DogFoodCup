from solid import *
from solid.utils import *
from solid.screw_thread import *

volumn = 354
h = 6
r = sqrt(volumn/(h*3.14))
thickness = 0.3
threads = thread([[0, -0.5], [0, 0], [-0.2, 0], [-0.2, -0.5]],r,1,h)


d = difference()(
    cylinder(r=r+thickness,h=h),
    up(thickness)(union()(threads,cylinder(r=r,h=h)))
)


print(r)
scad_render_to_file(d, 'dogfoodcup.scad', file_header = '$fn=180;')

