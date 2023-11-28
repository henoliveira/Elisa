import random
import sys
from time import sleep

import OpenGL.GL as gl
import OpenGL.GLU as glu
import OpenGL.GLUT as glut

from utils import (
    BASE_COLOR,
    COLORS_LIST,
    SCENE_COORDINATES,
    SCENE_COORDINATES_3D,
    TEXT_COLOR,
)

LIGHT_INTENSITY = 0.3  # Initial light intensity


class Polygons:
    def __init__(
        self,
        x: int,
        y: int,
        z: int,
        id: int,
        index: int,
    ):
        self.position = (x, y, z)
        self.id = id
        self.form_id = int(str(id)[0])
        self.color_id = int(str(id)[1])
        self.index = index
        self.parent_index = (index - 1) // 2
        self.children_indexes = []
        if index < 15:
            self.children_indexes = [index * 2 + 1, index * 2 + 2]
        gl.glShadeModel(gl.GL_FLAT)

    def display(self, active: bool = False):
        if active is False:
            gl.glColor3f(*COLORS_LIST[self.color_id])
        else:
            gl.glColor3f(*TEXT_COLOR)
            gl.glFlush()

        gl.glPushMatrix()
        gl.glTranslatef(*self.position)

        match self.form_id:
            case 1:
                glut.glutSolidCube(1.0)
            case 2:
                glut.glutSolidSphere(0.7, 20, 20)
            case 3:
                glut.glutSolidTeapot(0.6)
            case 4:
                glut.glutSolidOctahedron()

        gl.glPopMatrix()


class Scene:
    def __init__(self):
        self.rotate_y = 0.0
        self.rotate_x = 0.0
        self.translation_x = 0.0
        self.translation_y = 0.0
        self.scale = 0.2
        self.selected_scene = 0
        self.combinations = random.sample(range(10, 50), 31)

        selected_scene_coordinates = (
            SCENE_COORDINATES if self.selected_scene == 0 else SCENE_COORDINATES_3D
        )

        self.polygons = [
            Polygons(
                *selected_scene_coordinates[index],
                id=self.combinations[index],
                index=index,
            )
            for index in range(31)
        ]

        glut.glutInit(sys.argv)
        glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)  # type: ignore
        glut.glutInitWindowSize(800, 800)
        glut.glutCreateWindow("Polygons")

        glut.glutDisplayFunc(self.display)
        glut.glutReshapeFunc(self.reshape)
        glut.glutSpecialFunc(self.special)
        glut.glutKeyboardFunc(self.keyboard)

        gl.glEnable(gl.GL_LIGHTING)
        gl.glEnable(gl.GL_LIGHT0)

        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, [0.0, 0.0, -100.0, 1.0])
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, [10.0, 0.0, -100.0, 1.0])
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, [-10.0, 0.0, -100.0, 1.0])
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, [0.0, 10.0, -100.0, 1.0])
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, [0.0, -10.0, -100.0, 1.0])

        light_color = [1.0, 1.0, 1.0, 1.0]
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, light_color)
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_SPECULAR, light_color)

        gl.glEnable(gl.GL_COLOR_MATERIAL)
        gl.glColorMaterial(gl.GL_FRONT, gl.GL_AMBIENT_AND_DIFFUSE)

        self.polygons_dict = {
            1: "Cube",
            2: "Sphere",
            3: "Teapot",
            4: "Tetrahedron",
        }

        self.colors_dict = {
            0: "Blue",
            1: "Green",
            2: "Maroon",
            3: "Mauve",
            4: "Peach",
            5: "Pink",
            6: "Red",
            7: "Rosewater",
            8: "Sky",
            9: "Yellow",
        }

        self.selected_polygon = None
        self.selected_color = None

        self.create_menu()

        glut.glutPostRedisplay()
        glut.glutMainLoop()

    def create_menu(self):
        form_menu = glut.glutCreateMenu(self.form_menu_handler)
        glut.glutAddMenuEntry("Cubo", 1)
        glut.glutAddMenuEntry("Esfera", 2)
        glut.glutAddMenuEntry("Teapot", 3)
        glut.glutAddMenuEntry("Tetraedro", 4)

        color_menu = glut.glutCreateMenu(self.color_menu_handler)
        glut.glutAddMenuEntry("Azul", 0)
        glut.glutAddMenuEntry("Verde", 1)
        glut.glutAddMenuEntry("Maroon", 2)
        glut.glutAddMenuEntry("Malva", 3)
        glut.glutAddMenuEntry("Pessego", 4)
        glut.glutAddMenuEntry("Rosa", 5)
        glut.glutAddMenuEntry("Vermelho", 6)
        glut.glutAddMenuEntry("Rosa claro", 7)
        glut.glutAddMenuEntry("Azul claro", 8)
        glut.glutAddMenuEntry("Amarelo", 9)

        main_menu = glut.glutCreateMenu(self.menu_handler)
        glut.glutAddSubMenu("Selecionar forma", form_menu)
        glut.glutAddSubMenu("Selecionar cor", color_menu)
        glut.glutAddMenuEntry("Iniciar DFS", main_menu)

        glut.glutAttachMenu(glut.GLUT_RIGHT_BUTTON)

    def form_menu_handler(self, value):
        self.selected_polygon = value
        return value

    def color_menu_handler(self, value):
        self.selected_color = value
        return value

    def menu_handler(self, _):
        glut.glutPostRedisplay()
        self.start_dfs()

    def start_dfs(self):
        if self.selected_polygon == None or self.selected_color == None:
            print("Selecione um polígono e uma cor")
            return

        if self.dfs(self.polygons, self.polygons[0]):
            print(
                f"Encontrou {self.polygons_dict[self.selected_polygon]} {self.colors_dict[self.selected_color]}"
            )
        else:
            print(
                f"Não encontrou {self.polygons_dict[self.selected_polygon]} {self.colors_dict[self.selected_color]}"
            )

    def dfs(self, graph: list[Polygons], start_node: Polygons, visited=None) -> bool:
        start_node.display(True)
        sleep(1)
        target = int(str(self.selected_polygon) + str(self.selected_color))

        if visited is None:
            visited = set()

        visited.add(start_node.index)

        if start_node.id == target:
            print(visited)
            active = True
            for _ in range(20):
                start_node.display(active)
                sleep(0.5)
                active = not active
                glut.glutSwapBuffers()
                glut.glutPostRedisplay()
            return True

        for neighbor in start_node.children_indexes:
            if neighbor not in visited:
                if self.dfs(graph, graph[neighbor], visited):
                    return True

        return False

    def display(self):
        gl.glClearColor(*BASE_COLOR, 1.0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)
        gl.glLoadIdentity()
        glu.gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        gl.glRotatef(self.rotate_x, 1.0, 0.0, 0.0)
        gl.glRotatef(self.rotate_y, 0.0, 1.0, 0.0)
        gl.glScalef(self.scale, self.scale, self.scale)
        gl.glTranslatef(self.translation_x, self.translation_y, 0.0)

        selected_scene_coordinates = (
            SCENE_COORDINATES if self.selected_scene == 0 else SCENE_COORDINATES_3D
        )

        gl.glColor3f(LIGHT_INTENSITY, LIGHT_INTENSITY, LIGHT_INTENSITY)
        gl.glLightfv(
            gl.GL_LIGHT0,
            gl.GL_DIFFUSE,
            [LIGHT_INTENSITY, LIGHT_INTENSITY, LIGHT_INTENSITY, 1.0],
        )

        for polygon in self.polygons:
            polygon.display()
            if polygon.parent_index < 0:
                continue

            gl.glColor3f(*TEXT_COLOR)
            gl.glBegin(gl.GL_LINES)
            gl.glVertex3f(*selected_scene_coordinates[polygon.index])
            gl.glVertex3f(*selected_scene_coordinates[polygon.parent_index])

            gl.glEnd()

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

    def reDrawPolygons(self):
        self.combinations = random.sample(range(10, 50), 31)

        selected_scene_coordinates = (
            SCENE_COORDINATES if self.selected_scene == 0 else SCENE_COORDINATES_3D
        )

        self.polygons = [
            Polygons(
                *selected_scene_coordinates[index],
                id=self.combinations[index],
                index=index,
            )
            for index in range(31)
        ]

    def keyboard(self, key, x, y):
        global LIGHT_INTENSITY
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

        if key == b"z":
            self.selected_scene = 1
            self.reDrawPolygons()
            
        if key == b"x":
            self.selected_scene = 0
            self.reDrawPolygons()

        if key == b"l":
            LIGHT_INTENSITY += 0.1
            if LIGHT_INTENSITY > 1.0:
                LIGHT_INTENSITY = 0.0
        if key == b"k":
            LIGHT_INTENSITY -= 0.1
            if LIGHT_INTENSITY < 0.0:
                LIGHT_INTENSITY = 1.0

        glut.glutPostRedisplay()


if __name__ == "__main__":
    Scene()
