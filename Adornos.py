import math
from Modelo import *
import glm

class Rombos(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.posicion = glm.vec3(0.0,0.0,0.0)
        self.vertices = np.array(
            [
                #1
                -0.05,0.05,0.0,1.0,    0.0,0.0,1.0,1.0,  #izquierda arriba
                -0.05,-0.05,0.0,1.0,    0.0,0.0,1.0,1.0,  #izquierda abajo
                0.05,0.05,0.0,1.0,     0.0,0.0,1.0,1.0, #derecha arriba
                0.05,-0.05,0.0,1.0,    0.0,0.0,1.0,1.0, # derecha abajo

                

                #2
                -0.05,0.05,0.0,1.0,     0.368,0.380,1.0,1.0,  #izquierda arriba
                -0.05,-0.05,0.0,1.0,    0.368,0.380,1.0,1.0,  #izquierda abajo
                0.05,0.05,0.0,1.0,      0.368,0.380,1.0,1.0, #derecha arriba
                0.05,-0.05,0.0,1.0,     0.368,0.380,1.0,1.0, # derecha abajo

                
            ], dtype="float32"
        )

        self.posicion = glm.vec3(0,0,0)
        #crear una matriz identidad
        self.transformaciones = glm.mat4(1.0)
        #self.transformaciones = glm.translate(self.transformaciones,
        #            glm.vec3(0.5,-0.2,0.0))
        #self.transformaciones = glm.rotate(self.transformaciones,
        #            45.0, glm.vec3(0.0,0.0,1.0))
        super().__init__(shader, posicion_id, color_id, transformaciones_id)

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()