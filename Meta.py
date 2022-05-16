import math
from Modelo import *
import glm

class Meta(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.posicion = glm.vec3(0.0,0.0,0.0)
        self.vertices = np.array(
            [
                -0.05, 9.0, 0.0,1.0,     40/255, 50/255, 100/255,1.0,  #izquierda arriba
                -0.05,-0.05,0.0,1.0,    40/255, 50/255, 100/255,1.0,  #izquierda abajo
                0.05, 9.0, 0.0,1.0,      40/255, 50/255, 100/255,1.0, #derecha arriba
                0.05,-0.05,0.0,1.0,     40/255, 50/255, 100/255,1.0 # derecha abajo
                
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

    def mover(self, direccion):
        
        if direccion == self.ARRIBA:
           self.posicion.y  = self.posicion.y + 0.001
        elif direccion == self.ABAJO:
            self.posicion.y = self.posicion.y - 0.001

        self.transformaciones = glm.mat4(1.0)
        self.transformaciones = glm.translate(self.transformaciones,
                self.posicion)

    def dibujar(self):
        self.shader.usar_programa()
        gl.glBindVertexArray(self.VAO)

        gl.glUniformMatrix4fv(self.transformaciones_id,
                1, gl.GL_FALSE, glm.value_ptr(self.transformaciones))

        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        #gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 4, 4)
        #gl.glDrawArrays(gl.GL_TRIANGLE_FAN, 8, 74)

        gl.glBindVertexArray(0)
        self.shader.liberar_programa()