import sys
from ctypes import c_void_p

import numpy as np
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import utils as ut

WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 600

PROGRAM = None
VERTEX_ARRAY_OBJECT = None
VERTEX_BUFFER_OBJECT = None

VERTEX_SHADER = """
#version 330 core
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 color;

out vec3 vColor;

uniform mat4 transform;

void main()
{
    gl_Position = transform * vec4(position, 1.0);
    vColor = color;
}
"""

FRAGMENT_SHADER = """
#version 330 core

in vec3 vColor;
out vec4 FragColor;

void main()
{
    FragColor = vec4(vColor, 1.0f);
} 
"""

def display():

    gl.glClearColor(0.2, 0.3, 0.3, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    gl.glUseProgram(PROGRAM)
    gl.glBindVertexArray(VERTEX_ARRAY_OBJECT)

    # Translation. 
    T = ut.matTranslate(0.5, -0.5, 0.0)
    # Rotation around z-axis.
    Rz = ut.matRotateZ(np.radians(30.0))
    # Scale.
    S = ut.matScale(0.3, 0.5, 1.0)

    # M = T*R*S. 
    M = np.matmul(Rz,S)
    M = np.matmul(T,M)

    # Retrieve location of tranform variable in shader.
    loc = gl.glGetUniformLocation(PROGRAM, "transform");
    # Send matrix to shader.
    gl.glUniformMatrix4fv(loc, 1, gl.GL_FALSE, M.transpose())

    gl.glDrawArrays(gl.GL_TRIANGLES, 0, 6)

    glut.glutSwapBuffers()


def reshape(width,height):
    gl.glViewport(0, 0, width, height)
    glut.glutPostRedisplay()


def keyboard(key, x, y):

    global type_primitive

    if key == b'\x1b'or key == b'q':
        sys.exit( )
    if key == b'1':
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)
    if key == b'2':
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)

    glut.glutPostRedisplay()


def initData():

    # Uses vertex arrays.
    global VERTEX_ARRAY_OBJECT
    global VERTEX_BUFFER_OBJECT

    # Set vertices.
    vertices = np.array([
        # First triangle
        # coordinate     color
        -0.5, -0.5, 0.0, 0.0, 0.0, 1.0,
         0.5, -0.5, 0.0, 1.0, 1.0, 0.0,
        -0.5,  0.5, 0.0, 1.0, 0.0, 0.0,
        # Second triangle
        # coordinate     color
         0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
         0.5,  0.5, 0.0, 0.0, 1.0, 0.0,
        -0.5,  0.5, 0.0, 1.0, 0.0, 0.0
    ], dtype='float32')
    
    # Vertex array.
    VERTEX_ARRAY_OBJECT = gl.glGenVertexArrays(1)
    gl.glBindVertexArray(VERTEX_ARRAY_OBJECT)

    # Vertex buffer
    VERTEX_BUFFER_OBJECT = gl.glGenBuffers(1)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, VERTEX_BUFFER_OBJECT)
    gl.glBufferData(gl.GL_ARRAY_BUFFER, vertices.nbytes, vertices, gl.GL_STATIC_DRAW)
    
    # Set attributes.
    gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 6*vertices.itemsize, None)
    gl.glEnableVertexAttribArray(0)
    gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 6*vertices.itemsize, c_void_p(3*vertices.itemsize))
    gl.glEnableVertexAttribArray(1)
    
    gl.glBindVertexArray(0)

def initShaders():

    global PROGRAM

    PROGRAM = ut.createShaderProgram(VERTEX_SHADER, FRAGMENT_SHADER)


def main():

    glut.glutInit()
    glut.glutInitContextVersion(3, 3);
    glut.glutInitContextProfile(glut.GLUT_CORE_PROFILE);
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA) # type: ignore
    glut.glutInitWindowSize(WINDOW_WIDTH,WINDOW_HEIGHT)
    glut.glutCreateWindow('Geometric transformations')

    initData()
    initShaders()

    glut.glutReshapeFunc(reshape)
    glut.glutDisplayFunc(display)
    glut.glutKeyboardFunc(keyboard)

    glut.glutMainLoop()

if __name__ == '__main__':
    main()
