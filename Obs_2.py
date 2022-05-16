import math
from Modelo import *
import glm

class Obs_2(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):

        self.posicion = glm.vec3(-0.1, -0.55, 0.0)

        #Colisiones
        self.extremo_derecho = 0.15
        self.extremo_izquierdo = 0.05
        self.extremo_inferior = 0.05
        self.extremo_superior = 0.10

        self.vertices = np.array(
            [
                -0.05,0.05,0.0,1.0,    0.158,0.368,0.456,1.0,  #izquierda arriba
                -0.05,-0.05,0.0,1.0,    0.158,0.368,0.456,1.0,  #izquierda abajo
                0.05,0.05,0.0,1.0,      0.158,0.368,0.456,1.0, #derecha arriba
                0.05,-0.05,0.0,1.0,     0.158,0.368,0.456,1.0, # derecha abajo

                -0.05,0.15,0.0,1.0,     0.621,0.61,0.48,1.0,  #izquierda arriba
                -0.05,-0.05,0.0,1.0,     0.621,0.61,0.48,1.0,  #izquierda abajo
               0.05,0.15,0.0,1.0,      0.621,0.61,0.48,1.0, #derecha arriba
               0.05,-0.05,0.0,1.0,     0.621,0.61,0.48,1.0, # derecha abajo
                
            ], dtype="float32"
        )
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
            (self.posicion))

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()