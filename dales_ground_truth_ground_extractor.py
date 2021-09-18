import laspy
from dales_classes import DalesClasses

las = laspy.read('dales_las/train/5080_54435.las')
las.points = las.points[las.classification == DalesClasses.GROUND]
las.write('ground.las')