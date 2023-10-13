import sys

import OpenGL.GL as gl
import OpenGL.GLUT as glut

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def display():
    gl.glClearColor(0.2, 0.3, 0.3, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    glut.glutSwapBuffers()


def reshape(width, height):
    win_width = width
    win_height = height

    gl.glViewport(0, 0, width, height)
    glut.glutPostRedisplay()


def keyboard(key, x, y):
    if key == b"\x1b" or key == b"q":
        sys.exit()


def main():
    glut.glutInit()

    glut.glutInitContextVersion(3, 3)
    glut.glutInitContextProfile(glut.GLUT_CORE_PROFILE)

    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)  # type: ignore

    glut.glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)

    glut.glutCreateWindow("Window")

    glut.glutReshapeFunc(reshape)
    glut.glutDisplayFunc(display)
    glut.glutKeyboardFunc(keyboard)

    glut.glutMainLoop()


if __name__ == "__main__":
    main()
