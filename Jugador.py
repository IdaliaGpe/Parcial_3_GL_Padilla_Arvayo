import math
from Modelo import *
import glm
import glfw

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

        self.posicion_anterior = 0.0

        self.velocidad_y = 0.7

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

            #Salto
            #Velocidad de salto
            poder_salto = 1.9
            vel_y = self.velocidad_y * tiempo_delta * poder_salto
            gravedad = -0.9
            #Que tan alto salta
            cantidad_de_salto = 0.5

            estado_tecla_space = glfw.get_key(window, glfw.KEY_SPACE)
            #print(str(estado_tecla_space))

            if self.JUMP is False and self.IS_JUMPING is False and estado_tecla_space == glfw.PRESS:
                self.JUMP = True
                self.posicion_y_cuadrado_anterior = self.posicion[1]

            if self.JUMP is True:
                # Añade a la y la velocidad_y a la velocidad anteiror
                # Añade la velocidad del salto
                self.posicion[1] += vel_y
                self.IS_JUMPING = True

            #Ver si ya se paso
            if self.IS_JUMPING:
                if self.posicion[1] - self.posicion_y_cuadrado_anterior >= cantidad_de_salto:
                    
                    self.JUMP = False
                    vel_y = gravedad * tiempo_delta
                    self.posicion[1] += vel_y
                    self.IS_FALLING = True

            if self.IS_FALLING: 
                vel_y = gravedad * tiempo_delta
                self.posicion[1] += vel_y

                if self.posicion[1] <= self.posicion_y_cuadrado_anterior:
                    self.IS_JUMPING = False
                    self.JUMP = False
                    self.IS_FALLING = False
                    self.posicion[1] = self.posicion_y_cuadrado_anterior

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