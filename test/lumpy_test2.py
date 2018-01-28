#!/usr/bin/python
import Lumpy


lumpy = Lumpy.Lumpy()
lumpy.opaque_class(Lumpy.Gui)
lumpy.make_reference()

lumpy2 = Lumpy.Lumpy()

lumpy.object_diagram()
lumpy.class_diagram()

