import random
import sys

import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut
from utils import BASE_COLOR, COLORS, COLORS_LIST, SCENE_COORDINATES


class Polygons:
    def __init__(
        self,
        x: int,
        y: int,
        z: int,
        color_id: int,
        form: int,
    ):
        self.position = (x, y, z)
        self.color_id = color_id
        self.form = form
        gl.glShadeModel(gl.GL_FLAT)

    def display(self):
        gl.glPushMatrix()
        gl.glTranslatef(*self.position)
        gl.glColor3f(*COLORS_LIST[self.color_id])
        match self.form:
            case 1:
                glut.glutSolidCube(1.0)
            case 2:
                glut.glutSolidSphere(0.7, 20, 20)
            case 3:
                glut.glutSolidTeapot(0.6)
            case 4:
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
        self.polygons = [
            Polygons(
                *SCENE_COORDINATES[index],
                color_id=int(str(self.combinations[index])[1]),
                form=int(str(self.combinations[index])[0]),
            )
            for index in range(31)
        ]

        glut.glutInit(sys.argv)
        glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)  # type: ignore
        glut.glutInitWindowSize(800, 800)
        glut.glutCreateWindow("Multiple Cubes")

        glut.glutDisplayFunc(self.display)
        glut.glutReshapeFunc(self.reshape)
        glut.glutSpecialFunc(self.special)
        glut.glutKeyboardFunc(self.keyboard)
        glut.glutMainLoop()

    def display(self):
        gl.glClearColor(*BASE_COLOR, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glLoadIdentity()
        glu.gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        gl.glRotatef(self.rotate_x, 1.0, 0.0, 0.0)
        gl.glRotatef(self.rotate_y, 0.0, 1.0, 0.0)
        gl.glScalef(self.scale, self.scale, self.scale)
        gl.glTranslatef(self.translation_x, self.translation_y, 0.0)

        for polygon in self.polygons:
            polygon.display()

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
