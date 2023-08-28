
"""Turtle3D

Module turtle in space
"""


import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def rotation(P,v,theta):
    """ Rotation of P along an axe v = (vx,vy,vz), angle is theta """
    x, y, z = P
    vx, vy, vz = v
    cs, sn = np.cos(theta), np.sin(theta)
    X = (vx**2*(1-cs)+cs)*x    + (vx*vy*(1-cs)-vz*sn)*y + (vx*vz*(1-cs)+vy*sn)*z
    Y = (vx*vy*(1-cs)+vz*sn)*x + (vy**2*(1-cs)+cs)*y    + (vy*vz*(1-cs)-vx*sn)*z
    Z = (vx*vz*(1-cs)-vy*sn)*x + (vy*vz*(1-cs)+vx*sn)*y + (vz**2*(1-cs)+cs)*z
    return (X,Y,Z)

# Test
# P =(0,1,0)
# v = (0,0,1)
# Q = rotation(P,v,np.pi/2)
# print(Q)


class Turtle3D:

    def __init__(self):
        self.pos = (0,0,0)     # Position
        self.u = (1,0,0)       # Heading
        self.v = (0,1,0)       # Left
        self.isdown = True     # Is pen writing?
        self.segments = []     # List of segments to be traced

    def get_pos(self):
        return self.pos

    def get_u(self):
        return self.u  

    def get_v(self):
        return self.v

    def get_down(self):
        return self.isdown

    def get_segments(self):
        return self.segments

    def set_pos(self, newpos):
        self.pos = newpos

    def set_u(self, newu):
        self.u = newu

    def set_v(self, newv):
        self.v  =  newv

    def up(self):
        self.isdown = False  

    def down(self):
        self.isdown = True


    def get_w(self):
        """ (u,v,w) is an orthonormal direct basis """ 
        ux, uy, uz = self.u
        vx, vy, vz = self.v
        # Direct product:
        wx, wy, wz = uy*vz - vy*uz, uz*vx - vz*ux, ux*vy - vx*uy        
        return (wx,wy,wz)


    def forward(self, length):
        """ Move forward along vector u of the given length """
        x,y,z = self.get_pos()
        ux, uy, uz = self.u
        X, Y, Z = x+length*ux, y+length*uy, z+length*uz
        if self.isdown:
            self.segments.append( [(x,y,z), (X,Y,Z)] )
        self.set_pos( (X,Y,Z) )


    def goto(self, pos):
        """ Goto a fixed position (by drawing or not) """
        if self.isdown:
            self.segments += [self.pos, pos]
        self.set_pos( pos )


    def turn(self, theta):
        """ Turn = opposite(Yaw) = rotation around vertical axe w 
        (positive angle is turning left) """ 
        w = self.get_w()
        self.set_u( rotation(self.get_u(), w, theta) )       
        self.set_v( rotation(self.get_v(), w, theta) )       


    def roll(self, theta):
        """ Roll = rotation around axe u """ 
        self.set_v( rotation(self.get_v(), self.get_u(), theta) )       


    def pitch(self, theta):
        """ Pitch = Looking up or down = opposite(rotation around axe v) 
        positive angle is looking up """ 
        self.set_u( rotation(self.get_u(), self.get_v(), -theta) )       


    def show(self):
        """ Display list of successive positions following commands """
        fig = plt.figure()
        # ax = plt.axes(projection='3d')
        ax = plt.axes(projection='3d', proj_type = 'ortho')
        ax.set_xlabel('axe x')
        ax.set_ylabel('axe y')
        ax.set_zlabel('axe z')
        ax.view_init(30, -155)
        ax.set_xlim(-5,5)
        ax.set_ylim(-5,5)
        ax.set_zlim(0,10)

        list_segments = self.segments
        for P,Q in list_segments:
            # ax.scatter(*P, color='black')   
            # ax.scatter(*Q, color='black')
            ax.plot([P[0],Q[0]], [P[1],Q[1]], [P[2],Q[2]], color='black')   

        # ax.quiver( *self.get_pos(), *self.get_u(), length=0.2, color='blue' )
        # ax.quiver( *self.get_pos(), *self.get_v(), length=0.2, color='orange' )

        # plt.axis('off')
        plt.tight_layout()
        # plt.savefig('plante-01-0.png')
        plt.show()
        return


# Test
# t = Turtle3D()
# t.forward(1)
# t.turn(np.pi/4)
# t.forward(1)
# t.pitch(np.pi/6)
# t.forward(1)
# t.up()
# t.forward(1)
# t.down()
# t.forward(1)
# t.roll(np.pi/2)
# t.turn(np.pi/2)
# t.forward(1)
# print(t.get_segments())
# t.show()

