import math
from Modelo import *
import glm

class Fondo(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):

        self.posicion = glm.vec3(0.0, -0.90, 0.0)
        self.vertices = np.array(
            [    

                #Plataforma
                -1.0,0.30,0.0,1.0,     0.0, 0.0, 0.0,1.0,  #izquierda arriba
                -1.0,-0.30,0.0,1.0,    0.0, 0.0, 0.0,1.0,  #izquierda abajo
                1.0,0.30,0.0,1.0,     0.0, 0.0, 0.0,1.0, #derecha arriba
                1.0,-0.30,0.0,1.0,     0.0, 0.0, 0.0,1.0, # derecha abajo

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

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()