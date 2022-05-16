import math
from Modelo import *
import glm

class Jugador(Modelo):

    JUMP = False
    IS_JUMPING = False
    IS_FALLING = False
    herida = False
    posicion_y_cuadrado_anterior = 0.0

    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.posicion = glm.vec3(-0.9,-0.55,0.0)

        self.vertices = np.array(
            [
                -0.05,0.05,0.0,1.0,     0.4, 0.9, 0.21,1.0,  #izquierda arriba
                -0.05,-0.05,0.0,1.0,    0.4, 0.9, 0.21,1.0,  #izquierda abajo
                0.05,0.05,0.0,1.0,      0.4, 0.9, 0.21,1.0, #derecha arriba
                0.05,-0.05,0.0,1.0,     0.4, 0.9, 0.21,1.0 # derecha abajo
                
            ], dtype="float32"
        )

        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def mover(self, window, tiempo_delta):

            velocidad_cuadrado = 0.5

            cantidad_movimiento = velocidad_cuadrado * tiempo_delta

            #Cuadrado se mueve solo
            avanzar = True

            if avanzar == True:
                self.posicion[0] = self.posicion[0] + cantidad_movimiento

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
            (self.posicion))

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()