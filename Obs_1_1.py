import math
from Modelo import *
import glm

class Obs_1_1(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):

        self.posicion = glm.vec3(-0.5, -0.55, 0.0)

        self.vertices = np.array(
            [
                -0.05,-0.05, 0,1.0,     0.184,0.361,0.145,1.0,  #izquierda arriba
                0.0 ,0.05, 0,1.0,       0.184,0.361,0.145,1.0,  #izquierda abajo
                0.05,-0.05, 0,1.0,      0.184,0.361,0.145,1.0, #derecha arriba
                
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

        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 3)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()