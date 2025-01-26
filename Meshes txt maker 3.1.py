# ## This code was made by Mr. Jonathan Danieli for dr Amit Sitt's group. All rights reserved.
# Version 1-Can now makes squares and triangles
# Version 2- Can now let you save at a desired directory
# Version 3- can now also make monoclinics, Great thanks to Mr Elad Livnat.
#   Vesion 3.1- fixing a diagonal bug which made huge meshes a problem.

import numpy as np
import tkinter as tk
from tkinter import filedialog


def save_mesh(mesh_points):
    # Create a root Tkinter window
    root = tk.Tk()
    # Open file save dialog
    file_path = filedialog.asksaveasfilename(
        title="Save Mesh As",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    # Proceed if a valid file path is chosen
    if file_path:
        try:
            # Write the mesh points to the file
            with open(file_path, "w") as file:
                for point in mesh_points:
                    file.write("\t".join(map(str, point)) + "\n")
            print(f"Mesh saved to '{file_path}'.")
        except Exception as e:
            print(f"Error saving file: {e}")
    else:
        print("File save operation cancelled.")

    # Destroy the Tkinter root window
    root.destroy()




def generate_mesh(distance, shape, acceleration, velocity, center, junctions, layers,angle=None,distance2=None,distance3=None):
    """
    Generates a mesh and saves it to a text file.

    Parameters:
    - distance: The spacing between points in the mesh.
    - shape: The shape of the mesh ('triangle' or 'square').
    - acceleration: Acceleration value for all points.
    - velocity: Velocity value for all points.
    - center: Tuple (x_center, y_center) representing the center of the mesh.
    - layers: Number of layers for the mesh.
    """
    x_center, y_center = center
    mesh_points = []
    table_points=[]
    x_min=x_center-distance*junctions/2
    y_min=y_center-distance*junctions/2
    x_max=x_center+distance*junctions/2
    y_max=y_center+distance*junctions/2
    y_end_low=y_min-30
    y_end_high=y_max+30
    y_spike_low=y_min-20
    y_spike_middle_low=y_min-25
    y_spike_high=y_max+20
    y_spike_middle_high=y_max+25
    x_end_low=x_min-30
    x_end_high=x_max+30
    x_spike_low=x_min-20
    x_spike_middle_low=x_min-25
    x_spike_high=x_max+20
    x_spike_middle_high=x_max+25
    angle_radians = np.radians(angle)
    if shape == "square":
        for x in range(5):
            mesh_points.append((x_end_low, y_end_high, velocity, acceleration))
            mesh_points.append((x_end_low, y_end_low, velocity, acceleration))
        for dot in range(int(junctions)):  # PRINTING Y
            x = x_min + dot * distance
            if dot == 0:
                y_start = y_end_low
                y_end = y_spike_high
                table_points.append((x, y_start, velocity, acceleration))
                table_points.append((x, y_end, velocity, acceleration))
            elif dot // 2 == dot / 2:
                y_start = y_spike_low
                y_maximum = y_end_low
                y_end = y_spike_high
                table_points.append((x, y_start, velocity, acceleration))
                table_points.append((x, y_maximum, velocity, acceleration))
                table_points.append((x, y_end, velocity, acceleration))
            else:
                y_start = y_spike_high
                y_maximum = y_end_high
                y_end = y_spike_low
                table_points.append((x, y_start, velocity, acceleration))
                table_points.append((x, y_maximum, velocity, acceleration))
                table_points.append((x, y_end, velocity, acceleration))
        for dot in range(int(junctions)):  # PRINTING X
            y = y_min + dot * distance
            if dot == 0:
                x_start = x_end_high
                x_end = x_spike_low
                table_points.append((x_start, y, velocity, acceleration))
                table_points.append((x_end, y, velocity, acceleration))
            elif dot // 2 == dot / 2:
                x_start = x_spike_high
                x_maximum = x_end_high
                x_end = x_spike_low
                table_points.append((x_start, y, velocity, acceleration))
                table_points.append((x_maximum, y, velocity, acceleration))
                table_points.append((x_end, y, velocity, acceleration))
            else:
                x_start = x_spike_low
                x_maximum = x_end_low
                x_end = x_spike_high
                table_points.append((x_start, y, velocity, acceleration))
                table_points.append((x_maximum, y, velocity, acceleration))
                table_points.append((x_end, y, velocity, acceleration))
        mesh_points.extend(table_points)


    elif shape == "triangle":
        horizontal=[]
        diagonal1=[]
        diagonal2=[]
        for x in range(5):
                mesh_points.append((x_end_low, y_end_high, velocity, acceleration))
                mesh_points.append((x_end_low, y_end_low, velocity, acceleration))
        for dot in range(int(junctions)): #PRINTING X
            y=y_max-dot*distance
            if dot==0:
                x_start=x_end_low
                x_end=x_spike_high
                horizontal.append((x_start,y , velocity, acceleration))
                horizontal.append((x_end, y, velocity, acceleration))
            elif dot//2==dot/2:
                x_start=x_spike_low
                x_maximum=x_end_low
                x_end=x_spike_high
                horizontal.append((x_start,y , velocity, acceleration))
                horizontal.append((x_maximum,y , velocity, acceleration))
                horizontal.append((x_end,y , velocity, acceleration))
            else:
                x_start=x_spike_high
                x_maximum=x_end_high
                x_end=x_spike_low
                horizontal.append((x_start,y , velocity, acceleration))
                horizontal.append((x_maximum,y , velocity, acceleration))
                horizontal.append((x_end,y , velocity, acceleration))
        for row in horizontal:
            r=np.sqrt(row[0]**2+row[1]**2)
            if row[1]>0:
                theta=-np.arccos(row[0]/r)
                x1=r*np.cos(theta+np.pi/3)
                y1=r*np.sin(theta+np.pi/3)
                x2=r*np.cos(theta-np.pi/3)
                y2=r*np.sin(theta-np.pi/3)
                diagonal1.append((x1,y1 , velocity, acceleration))
                diagonal2.append((x2,y2 , velocity, acceleration))
            else:
                theta=np.arccos(row[0]/r)
                x1=r*np.cos(theta+np.pi/3)
                y1=r*np.sin(theta+np.pi/3)
                x2=r*np.cos(theta-np.pi/3)
                y2=r*np.sin(theta-np.pi/3)
                diagonal1.append((x1,y1 , velocity, acceleration))
                diagonal2.append((x2,y2 , velocity, acceleration))
        table_points.extend(horizontal)
        table_points.extend(diagonal1)
        table_points.extend(diagonal2)
        mesh_points.extend(table_points)
    elif shape == "monoclinic":
        horizontal=[]
        diagonal=[]
        diagonal_final=[]
        dist=distance-distance2
        h=distance2*np.sin(angle_radians)
        y_min=y_center-h*junctions/2
        y_max=y_center+h*junctions/2
        for x in range(5):
                mesh_points.append((x_end_low, y_end_high, velocity, acceleration))
                mesh_points.append((x_end_low, y_end_low, velocity, acceleration))
        for dot in range(int(junctions)): #PRINTING X
            y=y_max-dot*h
            if dot==0:
                x_start=x_end_low
                x_end=x_spike_high
                horizontal.append((x_start,y , velocity, acceleration))
                horizontal.append((x_end, y, velocity, acceleration))
            elif dot//2==dot/2:
                x_start=x_spike_low
                x_maximum=x_end_low
                x_end=x_spike_high
                horizontal.append((x_start,y , velocity, acceleration))
                horizontal.append((x_maximum,y , velocity, acceleration))
                horizontal.append((x_end,y , velocity, acceleration))
            else:
                x_start=x_spike_high
                x_maximum=x_end_high
                x_end=x_spike_low
                horizontal.append((x_start,y , velocity, acceleration))
                horizontal.append((x_maximum,y , velocity, acceleration))
                horizontal.append((x_end,y , velocity, acceleration))
        r1=np.sqrt(horizontal[0][0]**2+horizontal[0][1]**2)
        if horizontal[0][1]<0:
            theta1=-np.arccos(horizontal[0][0]/r1)
        else:
            theta1=np.arccos(horizontal[0][0]/r1)
        r2=np.sqrt(horizontal[1][0]**2+horizontal[1][1]**2)
        if horizontal[1][1]<0:
            theta2=-np.arccos(horizontal[1][0]/r2)
        else:
            theta2=np.arccos(horizontal[1][0]/r2)
        x_diagonal1=r1*np.cos(theta1+angle_radians)
        y_diagonal1=r1*np.sin(theta1+angle_radians)
        x_diagonal2=r2*np.cos(theta2+angle_radians)
        y_diagonal2=r2*np.sin(theta2+angle_radians)
        x_first_spike=x_diagonal2
        y_spike_up=y_diagonal2
        x_second_spike=x_diagonal1
        y_spike_down=y_diagonal1
        tail=5
        y_tail_up=y_diagonal2+5*np.sin(angle_radians)
        y_tail_down= y_diagonal1-5*np.sin(angle_radians)
        for dot in range(int(junctions)):
            if dot==0:
                diagonal.append((x_diagonal1, y_diagonal1 , velocity, acceleration))
                diagonal.append((x_diagonal2, y_diagonal2 , velocity, acceleration))
            elif dot//2==dot/2:
                x_start=x_second_spike+distance*dot
                x_tail=x_start-5*np.cos(angle_radians)
                x_end=x_first_spike+distance*dot
                diagonal.append((x_start,y_spike_down , velocity, acceleration))
                diagonal.append((x_tail,y_tail_down , velocity, acceleration))
                diagonal.append((x_end,y_spike_up ,velocity , acceleration))
            else:
                x_start=x_first_spike+distance*dot
                x_tail=x_start+5*np.cos(angle_radians)
                x_end= x_second_spike+distance*dot
                diagonal.append((x_start,y_spike_up , velocity, acceleration))
                diagonal.append((x_tail,y_tail_up , velocity, acceleration))
                diagonal.append((x_end,y_spike_down , velocity, acceleration))
        
        setoff_y=(y_tail_up+y_tail_down)/2
        x_count_min=0
        x_count_max=0
        for row in diagonal:
            if row[0]<x_count_min:
                x_count_min=row[0]
            elif row[0]>x_count_max:
                x_count_max=row[0]
        setoff_x=(x_count_min+x_count_max)/2
        for row in diagonal:
            x_new=row[0]-setoff_x+x_center
            y_new=row[1]-setoff_y+y_center
            diagonal_final.append((x_new, y_new , row[2], row[3]))
        table_points.extend(horizontal)
        table_points.extend(diagonal_final)
        mesh_points.extend(table_points)
        
    else:
        print("Invalid shape. Choose 'triangle', 'square' or 'monoclinic'.")
        return
    if layers>1:
        for layer in range(layers-1):
            mesh_points.extend(table_points)
    save_mesh(mesh_points)

# Example of how to use the function
if __name__ == "__main__":
    shape = input("Enter the shape ('triangle', 'square' or 'monoclinic'): ").lower()
    if shape=='monoclinic':
        angle = float(input("Enter the smaller angle in degrees: "))
        distance=float(input("Enter the long side's length in um: "))
        distance2=float(input("Enter the short side's length in um: "))
        distance3=0
    else:
        distance = float(input("Enter the side's length in um: "))
        distance2=0
        distance3=0
        angle=0
    acceleration = float(input("Enter the acceleration: "))
    velocity = float(input("Enter the velocity: "))
    center_x = float(input("Enter the x-coordinate of the center: "))
    center_y = float(input("Enter the y-coordinate of the center: "))
    junctions = float(input("Enter the number of junctions: "))
    layers = int(input("Enter the number of layers: "))
generate_mesh(distance/1000, shape, acceleration, velocity, (center_x, center_y), junctions, layers,angle,distance2/1000,distance3/1000)







