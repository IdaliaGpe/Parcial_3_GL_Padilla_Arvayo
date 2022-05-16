import math
from Modelo import *
import glm

class Fondo(Modelo):
    
    def __init__(self,shader, posicion_id, color_id, transformaciones_id):
        self.ARRIBA = 1
        self.ABAJO = 2
        self.IZQUIERDA = 3
        self.DERECHA = 4
        self.posicion = glm.vec3(0.0,0.0,0.0)
        self.vertices = np.array(
            [    
                #VERTICAL           
                #1
                -0.01,1.0,0.0,1.0,     0.628,0.121,1.0,1.0,  #izquierda arriba
                -0.01,-1.0,0.0,1.0,    0.628,0.121,1.0,1.0,  #izquierda abajo
                0.01,1.0,0.0,1.0,      0.628,0.121,1.0,1.0, #derecha arriba
                0.01,-1.0,0.0,1.0,     0.628,0.121,1.0,1.0, # derecha abajo

                #2
                -0.05,0.05,0.0,1.0,    0.0,0.0,1.0,1.0,  #izquierda arriba
                -0.05,-0.05,0.0,1.0,    0.0,0.0,1.0,1.0,  #izquierda abajo
                0.05,0.05,0.0,1.0,     0.0,0.0,1.0,1.0, #derecha arriba
                0.05,-0.05,0.0,1.0,    0.0,0.0,1.0,1.0, # derecha abajo

                #3
                -0.01,1.0,0.0,1.0,     0.628,0.121,1.0,1.0,  #izquierda arriba
                -0.01,-1.0,0.0,1.0,    0.628,0.121,1.0,1.0,  #izquierda abajo
                0.01,1.0,0.0,1.0,      0.628,0.121,1.0,1.0, #derecha arriba
                0.01,-1.0,0.0,1.0,     0.628,0.121,1.0,1.0, # derecha abajo

                #4
                -0.05,0.05,0.0,1.0,    0.0,0.0,1.0,1.0,  #izquierda arriba
                -0.05,-0.05,0.0,1.0,    0.0,0.0,1.0,1.0,  #izquierda abajo
                0.05,0.05,0.0,1.0,     0.0,0.0,1.0,1.0, #derecha arriba
                0.05,-0.05,0.0,1.0,    0.0,0.0,1.0,1.0, # derecha abajo

                #5
                -0.01,1.0,0.0,1.0,     0.628,0.121,1.0,1.0,  #izquierda arriba
                -0.01,-1.0,0.0,1.0,    0.628,0.121,1.0,1.0,  #izquierda abajo
                0.01,1.0,0.0,1.0,      0.628,0.121,1.0,1.0, #derecha arriba
                0.01,-1.0,0.0,1.0,     0.628,0.121,1.0,1.0, # derecha abajo

                #HORIZONTAL           
                #1
                -0.1,0.01,0.0,1.0,     0.628,0.121,1.0,1.0,  #izquierda arriba
               -0.1,-0.01,0.0,1.0,    0.628,0.121,1.0,1.0,  #izquierda abajo
                0.3,0.01,0.0,1.0,      0.628,0.121,1.0,1.0, #derecha arriba
                0.3,-0.01,0.0,1.0,     0.628,0.121,1.0,1.0, # derecha abajo

                #2
                -0.1,0.01,0.0,1.0,     0.628,0.121,1.0,1.0,  #izquierda arriba
               -0.1,-0.01,0.0,1.0,    0.628,0.121,1.0,1.0,  #izquierda abajo
                0.3,0.01,0.0,1.0,      0.628,0.121,1.0,1.0, #derecha arriba
                0.3,-0.01,0.0,1.0,     0.628,0.121,1.0,1.0, # derecha abajo

                #3
                -0.1,0.01,0.0,1.0,     0.628,0.121,1.0,1.0,  #izquierda arriba
               -0.1,-0.01,0.0,1.0,    0.628,0.121,1.0,1.0,  #izquierda abajo
                0.3,0.01,0.0,1.0,      0.628,0.121,1.0,1.0, #derecha arriba
                0.3,-0.01,0.0,1.0,     0.628,0.121,1.0,1.0, # derecha abajo

                #4
                -0.1,0.01,0.0,1.0,     0.628,0.121,1.0,1.0,  #izquierda arriba
               -0.1,-0.01,0.0,1.0,    0.628,0.121,1.0,1.0,  #izquierda abajo
                0.3,0.01,0.0,1.0,      0.628,0.121,1.0,1.0, #derecha arriba
                0.3,-0.01,0.0,1.0,     0.628,0.121,1.0,1.0, # derecha abajo

                #5
                -0.1,0.01,0.0,1.0,     0.628,0.121,1.0,1.0,  #izquierda arriba
               -0.1,-0.01,0.0,1.0,    0.628,0.121,1.0,1.0,  #izquierda abajo
                0.3,0.01,0.0,1.0,      0.628,0.121,1.0,1.0, #derecha arriba
                0.3,-0.01,0.0,1.0,     0.628,0.121,1.0,1.0, # derecha abajo

                #6
                -0.1,0.01,0.0,1.0,     0.628,0.121,1.0,1.0,  #izquierda arriba
               -0.1,-0.01,0.0,1.0,    0.628,0.121,1.0,1.0,  #izquierda abajo
                0.3,0.01,0.0,1.0,      0.628,0.121,1.0,1.0, #derecha arriba
                0.3,-0.01,0.0,1.0,     0.628,0.121,1.0,1.0, # derecha abajo

                #7
                -0.1,0.01,0.0,1.0,     0.628,0.121,1.0,1.0,  #izquierda arriba
               -0.1,-0.01,0.0,1.0,    0.628,0.121,1.0,1.0,  #izquierda abajo
                0.3,0.01,0.0,1.0,      0.628,0.121,1.0,1.0, #derecha arriba
                0.3,-0.01,0.0,1.0,     0.628,0.121,1.0,1.0, # derecha abajo

                #8
                -0.1,0.01,0.0,1.0,     0.628,0.121,1.0,1.0,  #izquierda arriba
               -0.1,-0.01,0.0,1.0,    0.628,0.121,1.0,1.0,  #izquierda abajo
                0.3,0.01,0.0,1.0,      0.628,0.121,1.0,1.0, #derecha arriba
                0.3,-0.01,0.0,1.0,     0.628,0.121,1.0,1.0, # derecha abajo

                #9
                -0.1,0.01,0.0,1.0,     0.628,0.121,1.0,1.0,  #izquierda arriba
               -0.1,-0.01,0.0,1.0,    0.628,0.121,1.0,1.0,  #izquierda abajo
                0.3,0.01,0.0,1.0,      0.628,0.121,1.0,1.0, #derecha arriba
                0.3,-0.01,0.0,1.0,     0.628,0.121,1.0,1.0, # derecha abajo
                #FIN LINEAS

                #FIGURA
                #Cuadrado
                -0.08,0.05,0.0,1.0,     0.167,0.003,0.359,1.0,  #izquierda arriba
               -0.08,-0.05,0.0,1.0,     0.167,0.003,0.359,1.0,  #izquierda abajo
                0.08,0.05,0.0,1.0,      0.167,0.003,0.359,1.0, #derecha arriba
                0.08,-0.05,0.0,1.0,     0.167,0.003,0.359,1.0, # derecha abajo

                #Cuadro grande morado
                -0.08,0.05,0.0,1.0,     0.167,0.003,0.359,1.0,  #izquierda arriba
               -0.08,-0.05,0.0,1.0,     0.167,0.003,0.359,1.0,  #izquierda abajo
                0.08,0.05,0.0,1.0,      0.167,0.003,0.359,1.0, #derecha arriba
                0.08,-0.05,0.0,1.0,     0.167,0.003,0.359,1.0, # derecha abajo

                #Plataforma
                -1.0,0.30,0.0,1.0,     0.0, 0.0, 0.0,1.0,  #izquierda arriba
                -1.0,-0.30,0.0,1.0,    0.0, 0.0, 0.0,1.0,  #izquierda abajo
                1.0,0.30,0.0,1.0,     0.0, 0.0, 0.0,1.0, #derecha arriba
                1.0,-0.30,0.0,1.0,     0.0, 0.0, 0.0,1.0, # derecha abajo

                #FIGURA
                #Triangulos
                #1
                -0.05,-0.05,0,1.0,     0.257,0.97,1,1.0,  #izquierda arriba
                0,0.05,0,1.0,          0.257,0.97,1,1.0,  #izquierda abajo
                0.05,-0.05,0,1.0,      0.257,0.97,1,1.0, #derecha arriba

                #2
                -0.05,-0.05,0,1.0,     0.127,0.072,0.506,1.0,  #izquierda arriba
                0,0.05,0,1.0,          0.127,0.072,0.506,1.0,  #izquierda abajo
                0.05,-0.05,0,1.0,      0.127,0.072,0.506,1.0, #derecha arriba

                #3
                -0.05,-0.05,0,1.0,     0.57,0.4,0.465,1.0,  #izquierda arriba
                0,0.05,0,1.0,          0.57,0.4,0.465,1.0,  #izquierda abajo
                0.05,-0.05,0,1.0,      0.57,0.4,0.465,1.0, #derecha arriba

                #4
                -0.05,-0.05,0,1.0,     0.21,0.42,0.691,1.0,  #izquierda arriba
                0,0.05,0,1.0,          0.21,0.42,0.691,1.0,  #izquierda abajo
                0.05,-0.05,0,1.0,      0.21,0.42,0.691,1.0, #derecha arrib

                #5
                -0.05,-0.05,0,1.0,     0.27,0.9,0.451,1.0,  #izquierda arriba
                0,0.05,0,1.0,          0.27,0.9,0.451,1.0,  #izquierda abajo
                0.05,-0.05,0,1.0,      0.27,0.9,0.451,1.0, #derecha arrib

                #6
                -0.05,-0.05,0,1.0,     0.2,0.972,0.851,1.0,  #izquierda arriba
                0,0.05,0,1.0,          0.2,0.972,0.851,1.0,  #izquierda abajo
                0.05,-0.05,0,1.0,      0.2,0.972,0.851,1.0, #derecha arrib

                
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
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 8, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 12, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 16, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 20, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 24, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 28, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 32, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 36, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 40, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 44, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 48, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 52, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 56, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 60, 4)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 64, 4)
        gl.glDrawArrays(gl.GL_TRIANGLES, 68, 3)
        gl.glDrawArrays(gl.GL_TRIANGLES, 71, 3)
        gl.glDrawArrays(gl.GL_TRIANGLES, 74, 3)
        gl.glDrawArrays(gl.GL_TRIANGLES, 77, 3)
        gl.glDrawArrays(gl.GL_TRIANGLES, 80, 3)
        gl.glDrawArrays(gl.GL_TRIANGLES, 83, 3)


        gl.glBindVertexArray(0)
        self.shader.liberar_programa()