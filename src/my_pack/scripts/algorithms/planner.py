#! /usr/bin/env/python3

import rospy
import random

def planner(start_index,goal_index, width, height, costrap, resolution, origin, costmap ,grid_viz  ):
     open_list =[]
     # open list contains the nodes, from which selection has to take place
     # Closes List contains the nodes, which have already been explored
     closed_list =set()
     #Pareets dictlonory pops on index to at's porent
     parents = dict()


     #ntesaltze current_Index and open_list
     Current_Index = start_index
     open_list.append(current_Index)
     #keep iterating vile there exists en element in opertlat
     while open_list:
          #stuffle open list and select the current_index
          #Shuffling ensures random selection

          random.shuffle(open_list)
          current_Index = open_list.pop(0)
     
          #add the current_index to closed_index
          closed_list.add(current_Index)
          #use grid_viz to set color to Rviz
          grid_viz.set_color(current_Index , "pink")
 
          #Break condition
          if current_Index== goal_index:
               break

          #Call function to get the nearsest neighbors
          #Returns neighbor Index along with cost to move to that neighbor
          neighbors = find_neighbors(current_Index, width, height, costmap, resolution)
          #Iterate over the neighbor indices
          for neighbor_index, _ in neighbors:
               # If neighbor index in Closed_List, already explored, nothing to do
               if neighbor_index in closed_list:
                    continue
               #Assign parent, useful when giving final path to rotot 
               parents[neighbor_index]= Current_Index
     
               #Append neighbor index to open_list (next nodes to choose from)
               open_list.append(neighbor_index)
#Extract the Path from the explored nodes, and finally return (Take care of the indentation)
     #Initialize list containing indices
     path=[]
     #Start With goal Indeax
     current_index = goal_index
     path.append (goal_index)
     #Iterate back starting from goal index, reaching till start
     # using the mapping derived from parents dictionary

     while current_index != start_index:
          current_Index = parents[current_Index]
          path.append (current_index)
     # Retunt reveresed path (starting fron start index, ending at goal index)
     return path[::-1]


def find_neighbors(index , width ,height ,costmap,orthogonal_step_cost):
     #--
     #identifles nelghbor nodes inspecting the Deceit melpoors
     #checks 1f nesenbor is inside che mo boundardes and 16 1s not an costacle ac Returns a list with walld neignboun sodes as (ledex, STRP_Cost) petro
     #--

     neighbors=[]
     #length of one diagonal  =length of one side by the square root of 2
     diagonal_Step_cost = orthogonal_step_cost * 1.41421
     #threshold value used to reject neighbor nodes as they are considered as obstacle 
     lethal_cost = 150
     # get the neighbor above the current cell
     upper = index - width
     if upper > 0:
          if costmap[upper] < lethal_cost:
               step_cost = orthogonal_step_cost + costmap[upper]/255
               neighbors.append([upper, step_cost])
     # get the neighbor to the Left of the current cell 
     left =index -1
     if left % width > 0:
          if costmap[left] < lethal_cost:
               step_cost = orthogonal_step_cost + costmap[left]/255
               neighbors.append([left, step_cost])

     #Get the helghoor to the top left of the current cell
     upper_left = index - width - 1
     if upper_left > 0 and upper_left % width > 0:
          if costmap[upper_left] < lethal_cost:
               step_cost = orthogonal_step_cost + costmap[upper_left]/255
               neighbors.append([index -width-1, step_cost])
    
     upper_right = index - width + 1
     if upper_right > 0 and upper_right % width != (width-1):
          if costmap[upper_right] < lethal_cost:
               step_cost = orthogonal_step_cost + costmap[upper_right]/255
               neighbors.append([index -width+1, step_cost])
     
     right= index + 1
     if right % width != (width+1):
          if costmap[right] < lethal_cost:
               step_cost = orthogonal_step_cost + costmap[right]/255
               neighbors.append([index +1 , step_cost])

     lower_left = index + width - 1
     if lower_left < height * width and lower_left % width != 0:
          if costmap[upper_left] < lethal_cost:
               step_cost = orthogonal_step_cost + costmap[upper_left]/255
               neighbors.append([index + width-1, step_cost])
     
     lower = index +width
     if lower<= height * width:
          if costmap[lower] < lethal_cost:
               step_cost=orthogonal_step_cost+costmap[lower]/255
               neighbors.append([lower,step_cost])
     
     lower_right=index+width+1
     if(lower_right) <= height*width and lower_right % width != (width -1):
          if costmap[lower_right]< lethal_cost:
               step_cost=diagonal_Step_cost+costmap[lower_right]/255
               neighbors.append([lower_right,step_cost])
     
     return neighbors