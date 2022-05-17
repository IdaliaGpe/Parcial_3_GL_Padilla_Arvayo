import math
from Modelo import *
from cmath import cos, pi, sin
import glm

class Cuadrado1(Modelo):
    
    fase = 90.0
    velocidad_cuadrado = 0.20
    angulo_triangulo = 0.0

    def __init__(self,shader, posicion_id, color_id, transformaciones_id):

        self.posicion = glm.vec3(0.0,-0.9, 0.0)
        self.direccion_cuadrado = 1
        self.posicion_anterior = 0.0
        self.scale = 0.5,0.5,0

        self.vertices = np.array(
            [
                #Rombo 2
                -0.05,0.05,0.0,1.0,     0.464, 0.393, 0.211,1.0,  #izquierda arriba
                -0.05,-0.05,0.0,1.0,    0.464, 0.393, 0.211,1.0,  #izquierda abajo
                0.05,0.05,0.0,1.0,      0.464, 0.393, 0.211,1.0, #derecha arriba
                0.05,-0.05,0.0,1.0,     0.464, 0.393, 0.211,1.0, # derecha abajo

            ], dtype="float32"
        )

        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def mover(self, tiempo_delta):

            cantidad_movimiento = self.velocidad_cuadrado * tiempo_delta

            if self.direccion_cuadrado == 0:
                self.posicion[0] = self.posicion[0] - cantidad_movimiento

            elif self.direccion_cuadrado == 1:
                self.posicion[0] = self.posicion[0] + cantidad_movimiento
            
            if self.posicion[0] <= -0.8 and self.direccion_cuadrado == 0:
                self.direccion_cuadrado = 1
            
            if self.posicion[0] >= 1 and self.direccion_cuadrado == 1:
                self.direccion_cuadrado = 0

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
            (self.posicion))

        self.transformaciones = glm.scale(self.transformaciones,
            (self.scale))

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()