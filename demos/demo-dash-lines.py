#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (C) 2013 Nicolas P. Rougier. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY NICOLAS P. ROUGIER ''AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL NICOLAS P. ROUGIER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# The views and conclusions contained in the software and documentation are
# those of the authors and should not be interpreted as representing official
# policies, either expressed or implied, of Nicolas P. Rougier.
# -----------------------------------------------------------------------------
import numpy as np
import OpenGL.GL as gl

def on_display():
    gl.glClearColor(1,1,1,1);
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    collection.draw()
    glut.glutSwapBuffers()
    
def on_reshape(width, height):
    gl.glViewport(0, 0, width, height)

def on_keyboard(key, x, y):
    if key == '\033': sys.exit()

def on_idle():
    n = len(collection)
    collection.rotate += 0.001

    global t, t0, frames
    t = glut.glutGet( glut.GLUT_ELAPSED_TIME )
    frames = frames + 1
    if t-t0 > 2500:
        print "FPS : %.2f (%d frames in %.2f second)" % (frames*1000.0/(t-t0), frames, (t-t0)/1000.0)
        t0, frames = t,0
    glut.glutPostRedisplay()



# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import sys
    import OpenGL.GLUT as glut
    from shapes import star, asterisk
    from glagg import PathCollection

    t0, frames, t = 0,0,0
    t0 = glut.glutGet(glut.GLUT_ELAPSED_TIME)

    glut.glutInit(sys.argv)
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(512, 512)
    glut.glutCreateWindow("Antialiased thick polylines")
    glut.glutDisplayFunc(on_display)
    glut.glutReshapeFunc(on_reshape)
    glut.glutKeyboardFunc(on_keyboard)
    glut.glutIdleFunc(on_idle)

    vertices = np.array( [(+0.0,+0.5), (+0.0,-0.5)] )
    collection = PathCollection()
    for i in range(500):
        theta = i*(5.5/180.0*np.pi)
        radius = 255-i*0.45
        x = 256 + np.cos(theta)*radius
        y = 256 + np.sin(theta)*radius
        scale = 20-15*i/float(500)
        collection.append(vertices, closed=False,
                          scale = scale, rotate = theta + np.pi/2, translate = (x,y),
                          dash_pattern = 'loosely dotted' )
    glut.glutMainLoop()
