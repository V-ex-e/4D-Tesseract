import pygame
import sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define vertices of the cube
vertices = (
    (0, 0, 0),
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 1),
    (1, 1, 1),
    (0, 1, 1)
)

# Define edges of the cube by connecting vertices
edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
)

def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (1920, 1080)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(150, (display[0] / display[1]), 0.1, 50.0)
    
    glTranslatef(0, 0, -10)  # Adjust the camera position

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()  # Save the transformation state for the first cube
        glRotatef(pygame.time.get_ticks() * 0.2, 0.5, 0.5, 0.5)  # Rotate the first cube (increased speed)
        glTranslatef(-.5,-.5,-.5)
        draw_cube()
        glPopMatrix()  # Restore the transformation state for the first cube


        glPushMatrix() 
        glTranslatef(-.5,-.5,-.5)
        glRotatef(pygame.time.get_ticks() * 4, -0.5, -0.5, -0.5) 
        draw_cube() 
        glPopMatrix() 

        
        glPushMatrix()  
        glTranslatef(-.5,-.5,-.5)
        glRotatef(-pygame.time.get_ticks() * 0.02, 0.5, 0.5, 0.5)  # Rotate the fourth cube in the opposite direction (increased speed)
        draw_cube()
        glPopMatrix()  # Restore the transformation state for the fourth cube
        #2nd

        glPushMatrix() 
        glScalef(2,2,2) 
        glRotatef(pygame.time.get_ticks() * 0.2, 0.5, 0.5, 0.5)  # Rotate the first cube (increased speed)
        glTranslatef(-.5,-.5,-.5)
        draw_cube()
        glPopMatrix()  


        glPushMatrix() 
        glScalef(2,2,2)
        glTranslatef(-.5,-.5,-.5)
        glRotatef(pygame.time.get_ticks() * 4, -0.5, -0.5, -0.5)  # Rotate the third cube (increased speed)
        draw_cube() 
        glPopMatrix() 

        
        glPushMatrix()  
        glScalef(2,2,2)
        glTranslatef(-.5,-.5,-.5)
        glRotatef(-pygame.time.get_ticks() * 0.02, 0.5, 0.5, 0.5)  # Rotate the fourth cube in the opposite direction (increased speed)
        draw_cube()
        glPopMatrix()  

        #2nd opposite spin 
        glPushMatrix() 
        glScalef(2,2,2) # Save the transformation state for the first cube
        glRotatef(pygame.time.get_ticks() * 0.2, -0.5, -0.5, -0.5)  
        glTranslatef(-.5,-.5,-.5)
        draw_cube()
        glPopMatrix()  # Restore the transformation state for the first cube


        glPushMatrix() 
        glScalef(2,2,2)
        glTranslatef(-.5,-.5,-.5)
        glRotatef(pygame.time.get_ticks() * 4, 0.5, 0.5, 0.5)  # Rotate the third cube (increased speed)
        draw_cube() 
        glPopMatrix() 

        
        glPushMatrix()  # Save the transformation state for the fourth cube
        glScalef(2,2,2)
        glTranslatef(-.5,-.5,-.5)
        glRotatef(-pygame.time.get_ticks() * 0.02, -0.5, -0.5, -0.5)  
        draw_cube()
        glPopMatrix()  

        for i in range(10):
            factor_1 = 2 * i
            scale_f = factor_1 * factor_1
            translate_f = scale_f / 1000000 * -1
            glPushMatrix()  # Save the transformation state for the fifth cube
            glScalef(scale_f, scale_f, 0)
            glTranslatef(translate_f, translate_f, translate_f)
            glRotatef(-pygame.time.get_ticks() * 0.02, 0.5, 0.5, 0.5)  # Rotate the fifth cube in the opposite direction (increased speed)
            draw_cube()
            glPopMatrix() 
            
        for i in range(10):
            factor_1 = -2 * i
            scale_f = -factor_1 * factor_1
            translate_f = scale_f / 1000000 * -1
            glPushMatrix()  # Save the transformation state for the fifth cube
            glScalef(scale_f, scale_f, 0)
            glTranslatef(translate_f, translate_f, translate_f)
            glRotatef(-pygame.time.get_ticks() * 0.02, 0.5, 0.5, 0.5)  
            draw_cube()
            glPopMatrix()  # Restore the transformation state for the fifth cube

        for b in range(10):
            factor_1 = 2 * b
            scale_f = factor_1 * factor_1
            translate_f = scale_f / 1000000 * -1
            glPushMatrix()  # Save the transformation state for the fifth cube
            glScalef(scale_f, scale_f, 0)
            glTranslatef(translate_f, translate_f, translate_f)
            glRotatef(-pygame.time.get_ticks() * -0.02, 0.5, 0.5, 0.5)  # Rotate the fifth cube in the opposite direction (increased speed)
            draw_cube()
            glPopMatrix()  # Restore the transformation state for the fifth cube
            
        for b in range(10):
            factor_1 = -2 * b
            scale_f = -factor_1 * factor_1
            translate_f = scale_f / 1000000 * -1
            glPushMatrix()  # Save the transformation state for the fifth cube
            glScalef(scale_f, scale_f, 0)
            glTranslatef(translate_f, translate_f, translate_f)
            glRotatef(-pygame.time.get_ticks() * -0.02, 0.5, 0.5, 0.5)  # Rotate the fifth cube in the opposite direction (increased speed)
            draw_cube()
            glPopMatrix()  # Restore the transformation state for the fifth cube


        


        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
