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
from Obs_2 import *
from Obs_3 import *
from Rombos import *
from Cuadrado import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

cuadrado = None
rombos = None
meta = None
obs_1 = None
obs_2 = None
obs_3 = None
jugador = None
fondo = None
modelo = None
window = None

vertex_shader_source = ""
with open('vertex_shader.glsl') as archivo:
    vertex_shader_source = archivo.readlines()

fragment_shader_source = ""
with open('fragment_shader.glsl') as archivo:
    fragment_shader_source = archivo.readlines()

def actualizar():
    global window
    estado_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    if estado_arriba == glfw.PRESS:
        modelo.mover(modelo.ARRIBA)
    if estado_abajo == glfw.PRESS:
        modelo.mover(modelo.ABAJO)

def dibujar():
    global modelo
    global jugador
    global fondo
    global meta
    global obs_1
    global obs_1
    global obs_3
    global rombos
    global cuadrado

    meta.dibujar()
    fondo.dibujar()
    jugador.dibujar()
    obs_1.dibujar()
    obs_2.dibujar()
    obs_3.dibujar()
    rombos.dibujar()
    cuadrado.dibujar()

def main():
    global modelo
    global window
    global jugador
    global fondo
    global meta
    global obs_1
    global obs_2
    global obs_3
    global rombos
    global cuadrado

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

    obs_2 = Obs_2(shader,
        posicion_id, color_id, transformaciones_id)

    obs_3 = Obs_3(shader,
        posicion_id, color_id, transformaciones_id)

    rombos = Rombos(shader,
        posicion_id, color_id, transformaciones_id)

    cuadrado = Cuadrado(shader,
        posicion_id, color_id, transformaciones_id)

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
    obs_2.borrar()
    obs_3.borrar()
    rombos.borrar()
    cuadrado.borrar()

    glfw.terminate()
    return 0

def framebuffer_size_callbak(window, width, height):
    gl.glViewport(0,0,width,height)

if __name__ == '__main__':
    main()