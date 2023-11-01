import pygame, math, sys, random
import numpy as np

pygame.init()

width = 1000.0
height = 800.0

white = (255,255,255)
red = (255,0,0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0,0,0)
D_Grey = (30, 30, 30)

screen = pygame.display.set_mode((width, height))

degree = -10

clock = pygame.time.Clock()

FPS = 300

x4 = 500
y4 = 400

t,u = -1,-1

lines = []

for i in range(6):
    ln = [random.randrange(0,width),random.randrange(0,height),random.randrange(0,width),random.randrange(0,height)]
    lines.append(ln)


points = [[x4,y4]]

linecolor = (255,255,255)

count = 0

while True:

    count = count + 1 

    if np.array_equal(np.array(linecolor), np.array(D_Grey)):
        count = 0

    #print(count)
    if count >= 5:
        sub = (1,1,1)

        linecolor = np.array(linecolor) - np.array(sub)
        count = 0

    screen.fill(D_Grey)

    x3 = points[-1][0]
    y3 = points[-1][1]

    x4 += math.cos((math.radians(degree)))
    y4 += math.sin((math.radians(degree)))

    p = [x4,y4]

    points.append(p)

    if len(points) >= 1000:
        points.pop(0)
   

    for l in lines:

        x1 = l[0]
        y1 = l[1]
        x2 = l[2]
        y2 = l[3]

        if (x1 - x2) != 0:
            line_angle = math.degrees(math.atan((y1-y2)/(x1-x2)))

        if (x1 - x2) == 0:
            line_angle = 90
    

        pygame.draw.line(screen, white, (x1, y1), (x2, y2))
        

        if ((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))!=0:
            t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4))/((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))
            u = ((x1 - x3)*(y1 - y2) - (y1 - y3)*(x1 - x2))/((x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4))


        if 0<=t<=1 and 0<=u<=1:

            points.pop(-1)
            points.pop(-1)

            print("Collision")

            px = x1 + t*(x2-x1)
            py = y1 + t*(y2-y1)

            intersection = [px,py]
            degree = line_angle+(line_angle-degree)

    
    
    



    pygame.draw.lines(screen, linecolor, False, points)

    if pygame.event.get(pygame.QUIT):
        sys.exit()

    clock.tick(FPS)


    
    pygame.display.update()