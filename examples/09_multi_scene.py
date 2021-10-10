#!/usr/bin/env python

# Copyright (c) CTU  - All Rights Reserved
# Created on: 5/4/20
#     Author: Vladimir Petrik <vladimir.petrik@cvut.cz>

from pyphysx import *
from pyphysx_utils.rate import Rate
from pyphysx_render.pyrender import PyPhysxViewer


numScenes = 256
scenes = [None] * numScenes


for i in range(0,numScenes):
    scene = Scene()
    scene.add_actor(RigidStatic.create_plane(material=Material(static_friction=0.1, dynamic_friction=0.1, restitution=0.5)))
    scene.set_gravity([0,0,-9.81])
    
    for j in range(0,50):
        actor = RigidDynamic()
        actor.attach_shape(Shape.create_box([0.2] * 3, Material(restitution=1.)))
        actor.set_global_pose([0.5, 0.5, 0.2 + 0.2*j])
        actor.set_mass(1.)
        scene.add_actor(actor)



    scenes[i] = scene


render = PyPhysxViewer()
render.add_physx_scene(scenes[0])

rate = Rate(240)
it = 0

while render.is_active:
    for i in range(0,numScenes):
        scenes[i].simulate(rate.period(), block=False)

    for i in range(0,numScenes):
        scenes[i].fetch_results(True)

    print("simming.." + str(it))
    it = it + 1
    render.update(True)
    rate.sleep()
    
