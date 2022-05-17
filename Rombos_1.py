import math
from Modelo import *
import glm

class Rombos_1(Modelo):
    
    velocidad_angular = 135.0 
    rotacion = 0

    def __init__(self,shader, posicion_id, color_id, transformaciones_id):

        self.posicion = glm.vec3(-0.6, 0.05, 0.0)
        self.scale = glm.vec3(1.9,1.9,0)
        self.rotate = glm.vec3(0.0,0.0,1.0)

        self.vertices = np.array(
            [
                #Rombo 2
                -0.05,0.05,0.0,1.0,     0.368,0.380,1.0,1.0,  #izquierda arriba
                -0.05,-0.05,0.0,1.0,    0.368,0.380,1.0,1.0,  #izquierda abajo
                0.05,0.05,0.0,1.0,      0.368,0.380,1.0,1.0, #derecha arriba
                0.05,-0.05,0.0,1.0,     0.368,0.380,1.0,1.0, # derecha abajo

                
            ], dtype="float32"
        )

        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def rotar(self, tiempo_delta):

        cantidad_rotacion1 = -self.velocidad_angular * tiempo_delta
        self.rotacion = self.rotacion + cantidad_rotacion1

        if self.rotacion  > 360.0:
               self.rotacion = self.rotacion - 360.0


    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        self.transformaciones = glm.mat4(1.0)

        self.transformaciones = glm.translate(self.transformaciones,
            (self.posicion))

        self.transformaciones = glm.scale(self.transformaciones,
            (self.scale))
        
        self.transformaciones = glm.rotate(self.transformaciones,
                    self.rotacion, self.rotate)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()