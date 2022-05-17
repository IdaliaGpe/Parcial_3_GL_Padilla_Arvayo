from tkinter.messagebox import NO
import OpenGL.GL as gl
import glfw
import numpy as np
from Meta import *
from Shader import *
from Modelo import *
from Triangulo import Triangulo
from Jugador import *
from Fondo import *
from Obs_1 import *
from Obs_1_1 import *
from Obs_2 import *
from Obs_2_2 import *
from Obs_3 import *
from Obs_3_3 import *
from Rombos import *
from Rombos_1 import *
from Cuadrado import *
from Cuadrado1 import *

from Fondo_Line import *
from Fondo_Line1 import *
from Fondo_Line2 import *
from Fondo_Line3 import *
from Fondo_Line4 import *
from Fondo_Line5 import *
from Fondo_Line6 import *
from Fondo_Line7 import *
from Fondo_Line8 import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

cuadrado = None
cuadrado1 = None
rombos = None
rombos_1 = None
meta = None
obs_1 = None
obs_1_1 = None
obs_2 = None
obs_2_2 = None
obs_3 = None
obs_3_3 = None
jugador = None
fondo = None
modelo = None

fondo_line = None
fondo_line1 = None
fondo_line2 = None
fondo_line3 = None
fondo_line4 = None
fondo_line5 = None
fondo_line6 = None
fondo_line7 = None
fondo_line8 = None

window = None

tiempo_anterior = 0.0

closed = False
close = glfw.set_window_should_close(window, 1)

vertex_shader_source = ""
with open('vertex_shader.glsl') as archivo:
    vertex_shader_source = archivo.readlines()

fragment_shader_source = ""
with open('fragment_shader.glsl') as archivo:
    fragment_shader_source = archivo.readlines()

def key_callback(window, key, scancode, action, mods):
    #Que la tecla escape cierre ventana al ser presionado
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
         glfw.set_window_should_close(window, 1)

def actualizar():
    global tiempo_anterior
    global window

    tiempo_actual = glfw.get_time()
    # Cuanto tiempo paso entre la ejecucion actual
    # y la inmediata anterior de esta funcion
    tiempo_delta = tiempo_actual - tiempo_anterior

    jugador.mover(window, tiempo_delta)

    if jugador.colisionando(meta):
        glfw.set_window_should_close(window, 1)

    if jugador.colisionando(obs_1):
        jugador.posicion[0] = -0.9
    
    if jugador.colisionando(obs_2):
        jugador.posicion[0] = -0.9

    if jugador.colisionando(obs_3):
        jugador.posicion[0] = -0.9

    rombos.rotar(tiempo_delta)
    rombos_1.rotar(tiempo_delta)
    
    cuadrado.mover(tiempo_delta)
    cuadrado1.mover(tiempo_delta)

    tiempo_anterior = tiempo_actual

def colisionando():
    colisionando = False
    return colisionando   

def dibujar():
    global modelo
    global jugador
    global fondo
    global meta
    global obs_1
    global obs_1_1
    global obs_2
    global obs_2_2
    global obs_3
    global obs_3_3
    global rombos
    global rombos_1
    global cuadrado
    global cuadrado1

    global fondo_line
    global fondo_line1
    global fondo_line2
    global fondo_line3
    global fondo_line4
    global fondo_line5
    global fondo_line6
    global fondo_line7
    global fondo_line8

    fondo_line.dibujar()
    fondo_line1.dibujar()
    fondo_line2.dibujar()
    fondo_line3.dibujar()
    fondo_line4.dibujar()
    fondo_line5.dibujar()
    fondo_line6.dibujar()
    fondo_line7.dibujar()
    fondo_line8.dibujar()

    meta.dibujar()
    fondo.dibujar()
    obs_1.dibujar()
    obs_1_1.dibujar()
    obs_2.dibujar()
    obs_2_2.dibujar()
    obs_3.dibujar()
    obs_3_3.dibujar()
    rombos.dibujar()
    rombos_1.dibujar()
    cuadrado.dibujar()
    cuadrado1.dibujar()
    jugador.dibujar()


def main():

    global fondo_line
    global fondo_line1
    global fondo_line2
    global fondo_line3
    global fondo_line4
    global fondo_line5
    global fondo_line6
    global fondo_line7
    global fondo_line8

    global modelo
    global window
    global jugador
    global fondo
    global meta
    global obs_1
    global obs_1_1
    global obs_2
    global obs_2_2
    global obs_3
    global obs_3_3
    global rombos
    global rombos_1
    global cuadrado
    global cuadrado1

    glfw.init()

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, 
        "Geometry Dash Pirata",None,None)
    if window is None:
        glfw.terminate()
        raise Exception("No se pudo crear ventana")
    
    glfw.make_context_current(window)
    glfw.set_framebuffer_size_callback(window, framebuffer_size_callbak)

   
    shader = Shader(vertex_shader_source, fragment_shader_source)

    posicion_id = gl.glGetAttribLocation(shader.shader_program, "position")
    color_id = gl.glGetAttribLocation(shader.shader_program, "color")
    
    transformaciones_id = gl.glGetUniformLocation(
            shader.shader_program, "transformations")
    
    modelo = Triangulo(shader, 
            posicion_id, color_id, transformaciones_id)

    meta = Meta(shader,
            posicion_id, color_id, transformaciones_id)

    jugador = Jugador(shader,
        posicion_id, color_id, transformaciones_id)

    fondo = Fondo(shader,
        posicion_id, color_id, transformaciones_id)

    obs_1 = Obs_1(shader,
        posicion_id, color_id, transformaciones_id)

    obs_1_1 = Obs_1_1(shader,
        posicion_id, color_id, transformaciones_id)

    obs_2 = Obs_2(shader,
        posicion_id, color_id, transformaciones_id)
    
    obs_2_2 = Obs_2_2(shader,
        posicion_id, color_id, transformaciones_id)

    obs_3 = Obs_3(shader,
        posicion_id, color_id, transformaciones_id)

    obs_3_3 = Obs_3_3(shader,
        posicion_id, color_id, transformaciones_id)

    rombos = Rombos(shader,
        posicion_id, color_id, transformaciones_id)

    rombos_1 = Rombos_1(shader,
        posicion_id, color_id, transformaciones_id)

    cuadrado = Cuadrado(shader,
        posicion_id, color_id, transformaciones_id)

    cuadrado1 = Cuadrado(shader,
        posicion_id, color_id, transformaciones_id)



    fondo_line = Fondo_Line(shader,
        posicion_id, color_id, transformaciones_id)

    fondo_line1 = Fondo_Line1(shader,
        posicion_id, color_id, transformaciones_id)

    fondo_line2 = Fondo_Line2(shader,
        posicion_id, color_id, transformaciones_id)

    fondo_line3 = Fondo_Line3(shader,
        posicion_id, color_id, transformaciones_id)
    
    fondo_line4 = Fondo_Line4(shader,
        posicion_id, color_id, transformaciones_id)

    fondo_line5 = Fondo_Line5(shader,
        posicion_id, color_id, transformaciones_id)

    fondo_line6 = Fondo_Line6(shader,
        posicion_id, color_id, transformaciones_id)

    fondo_line7 = Fondo_Line7(shader,
        posicion_id, color_id, transformaciones_id)

    fondo_line8 = Fondo_Line8(shader,
        posicion_id, color_id, transformaciones_id)

    #Cerrar con ESC
    glfw.set_key_callback(window, key_callback)

    #draw loop
    while not glfw.window_should_close(window):
        gl.glClearColor(41/255, 44/255, 76/255, 1)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        #dibujar
        dibujar()
        actualizar()

        glfw.swap_buffers(window)
        glfw.poll_events()

    #Liberar memoria
    modelo.borrar()
    jugador.borrar()
    shader.borrar()
    meta.borrar()
    fondo.borrar()
    obs_1.borrar()
    obs_1_1.borrar()
    obs_2.borrar()
    obs_2_2.borrar()
    obs_3.borrar()
    obs_3_3.borrar()
    rombos.borrar()
    rombos_1.borrar()
    cuadrado.borrar()
    cuadrado1.borrar()

    fondo_line.borrar()
    fondo_line1.borrar()
    fondo_line2.borrar()
    fondo_line3.borrar()
    fondo_line4.borrar()
    fondo_line5.borrar()
    fondo_line6.borrar()
    fondo_line7.borrar()
    fondo_line8.borrar()

    glfw.terminate()
    return 0

def framebuffer_size_callbak(window, width, height):
    gl.glViewport(0,0,width,height)

if __name__ == '__main__':
    main()