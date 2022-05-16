import OpenGL.GL as gl
import numpy as np
from ctypes import c_void_p
import glm

class Modelo:

    def __init__(self, shader, posicion_id, color_id, transformaciones_id):
        self.shader = shader
        self.transformaciones_id = transformaciones_id
        #Generar vertex array object y vertex buffer object
        self.VAO = gl.glGenVertexArrays(1)
        self.VBO = gl.glGenBuffers(1)

        #Le decimos a OpenGL con cual VAO trabajar
        gl.glBindVertexArray(self.VAO)
        #Le decimos a OpenGL con cual Buffer trabajar
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, self.VBO)
        #Establecerle la información al buffer
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, 
            gl.GL_STATIC_DRAW)
        #Definir como leer el VAO y activarlo
        #posicion
        gl.glVertexAttribPointer(posicion_id, 4, gl.GL_FLOAT, 
            gl.GL_FALSE, 8 * self.vertices.itemsize , c_void_p(0))
        gl.glEnableVertexAttribArray(posicion_id)
        #color
        gl.glVertexAttribPointer(color_id, 4, gl.GL_FLOAT,
            gl.GL_FALSE, 8 * self.vertices.itemsize, 
            c_void_p(4 * self.vertices.itemsize))
        gl.glEnableVertexAttribArray(color_id)

        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
        gl.glBindVertexArray(0)

    def borrar(self):
        gl.glDeleteVertexArrays(1, self.VAO)
        gl.glDeleteBuffers(1, self.VBO)

    #POSICIONES
    @property
    def posicion(self):
        return self._posicion
    @posicion.setter
    def posicion(self, posicion):
        self._posicion = posicion

    #EXTREMOS
    @property
    def extremo_izquierdo(self):
        return self._extremo_izquierdo
    @extremo_izquierdo.setter
    def extremo_izquierdo(self, extremo_izquierdo):
        self._extremo_izquierdo = extremo_izquierdo

    @property
    def extremo_derecho(self):
        return self._extremo_derecho
    @extremo_derecho.setter
    def extremo_derecho(self, extremo_derecho):
        self._extremo_derecho = extremo_derecho

    @property
    def extremo_superior(self):
        return self._extremo_superior
    @extremo_superior.setter
    def extremo_superior(self, extremo_superior):
        self._extremo_superior = extremo_superior   

    @property
    def extremo_inferior(self):
        return self._extremo_inferior
    @extremo_inferior.setter
    def extremo_inferior(self, extremo_inferior):
        self._extremo_inferior = extremo_inferior

    def colisionando(self, modelo):
       
        assert isinstance(modelo, Modelo)
        colisionando = False

        if (self.posicion[0] + self.extremo_derecho >= modelo.posicion[0] - modelo.extremo_izquierdo
            and self.posicion[0] - self.extremo_izquierdo <= modelo.posicion[0] + modelo.extremo_derecho
            and self.posicion[1] + self.extremo_superior >= modelo.posicion[1] - modelo.extremo_inferior
            and self.posicion[1] - self.extremo_inferior <= modelo.posicion[1] + modelo.extremo_superior):

            colisionando = True

        return colisionando