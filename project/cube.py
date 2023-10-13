import random
import sys

import colors
import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
from generate import scene_coordinates


class Polygons:
    def __init__(self, x: int, y: int, z: int, color:int, form: int):
        self.position = (x, y, z)
        self.color = color
        gl.glShadeModel(gl.GL_FLAT)

    def display(self):
        gl.glPushMatrix()
        gl.glTranslatef(*self.position)
        gl.glColor3f(*self.color)
        # glut.glutSolidCube(1.0)
        # glut.glutSolidSphere(0.5, 20, 20)
        # glut.glutSolidTeapot(0.5)
        glut.glutSolidTetrahedron()
        gl.glPopMatrix()


class Scene:
    def __init__(self):
        self.rotate_y = 0.0
        self.rotate_x = 0.0
        self.translation_x = 0.0
        self.translation_y = 0.0
        self.scale = 0.2
        self.combinations = random.sample(range(10, 50), 31)
        # self.cubes = [
        #     Polygons(
        #         *coordinates,
        #         color=colors.randomly(),
        #         combination=combination,
        #     )
        #     for coordinates in scene_coordinates
        #     for combination in self.combinations
        # ]

        glut.glutInit(sys.argv)
        glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)  # type: ignore
        glut.glutInitWindowSize(800, 800)
        glut.glutCreateWindow("Multiple Cubes")

        glut.glutDisplayFunc(self.display)
        glut.glutReshapeFunc(self.reshape)
        glut.glutSpecialFunc(self.special)
        glut.glutKeyboardFunc(self.keyboard)
        glut.glutMainLoop()

    def generate_polygons(self):
        for 


    def display(self):
        gl.glClearColor(*colors.BASE, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glLoadIdentity()
        glu.gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        gl.glRotatef(self.rotate_x, 1.0, 0.0, 0.0)
        gl.glRotatef(self.rotate_y, 0.0, 1.0, 0.0)
        gl.glScalef(self.scale, self.scale, self.scale)
        gl.glTranslatef(self.translation_x, self.translation_y, 0.0)

        for cube in self.cubes:
            cube.display()

        gl.glFlush()

    def reshape(self, w, h):
        gl.glViewport(0, 0, glu.GLsizei(w), glu.GLsizei(h))
        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)

    def special(self, key, x, y):
        if key == glut.GLUT_KEY_RIGHT:
            self.rotate_y += 5
        if key == glut.GLUT_KEY_LEFT:
            self.rotate_y -= 5
        if key == glut.GLUT_KEY_UP:
            self.rotate_x += 5
        if key == glut.GLUT_KEY_DOWN:
            self.rotate_x -= 5
        glut.glutPostRedisplay()

    def keyboard(self, key, x, y):
        if key == b"d":
            self.translation_x -= 0.1
        if key == b"a":
            self.translation_x += 0.1
        if key == b"s":
            self.translation_y += 0.1
        if key == b"w":
            self.translation_y -= 0.1

        if key == b"[":
            self.scale -= 0.1
        if key == b"]":
            self.scale += 0.1

        glut.glutPostRedisplay()


if __name__ == "__main__":
    Scene()