b0VIM 8.1      hYV`�  �  iamgenius                               aadi                                    ~iamgenius/Desktop/Bug Fix/Python Files/cubemesh.py                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          utf-8U3210    #"! U                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 tp                                       t                            1       �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ad    \            �  �  �  �  �  �  �  �  �  �  �  �  ]  \  :  9       �  �  �  �  �  �  �  y  o  P  ;    �  �  �  �  �  �  F  $  �  �  �  �  �  �  �  Z  F  E  D  7    �  �  Y  9  8  �
  �
  �
  �
  �
  �
  n
  2
  �	  �	  �	  �	  	  ~	  }	  q	  E	  	  �  �  s  r  4  %  $  #    �  �  m  1      �  �  �  �  �  �  P    �  �  �  �  v  u  t  b  K  J  �  �  �  �  �  �  v  A    �  �  �  y  i  h  g  [  /  �  �  �  o  n  (          cube[Sides.bottom, :, :] = np.rot90(cube[Sides.bottom, :, :], -1)      cube[Sides.right, :, 0] = tmp     cube[Sides.back, :, 0] = cube[Sides.right, :, 0]     cube[Sides.left, :, 0] = cube[Sides.back, :, 0]     cube[Sides.front, :, 0] = cube[Sides.left, :, 0]     tmp = np.array(cube[Sides.front, :, 0]) def down():       return "U'"     cube[Sides.top, :, :] = np.rot90(cube[Sides.top, :, :])      cube[Sides.right, :, 0] = tmp     cube[Sides.back, :, 2] = cube[Sides.right, :, 2]     cube[Sides.left, :, 2] = cube[Sides.back, :, 2]     cube[Sides.front, :, 2] = cube[Sides.left, :, 2]     tmp = np.array(cube[Sides.front, :, 0])     time.sleep(2)     print("Moves applied: " + str(x) + "x \n") def randomization():   x = int(input("Wie oft sollen random Moves auf den Würfel ausgeübt werden?"))  from cubemesh import * def up_counter():       return "U"     cube[Sides.top, :, :] = np.rot90(cube[Sides.top, :, :], -1)      cube[Sides.left, :, 0] = tmp     cube[Sides.back, :, 2] = cube[Sides.left, :, 2]     cube[Sides.right, :, 2] = cube[Sides.back, :, 2]     cube[Sides.front, :, 2] = cube[Sides.right, :, 2]     tmp = np.array(cube[Sides.front, :, 0]) def up():       return "L'"     cube[Sides.left, :, :] = np.rot90(cube[Sides.left, :, :], -1)      cube[Sides.top, 0, :] = tmp     cube[Sides.back, 2, :] = np.flip(cube[Sides.top, 0, :])     cube[Sides.bottom, 0, :] = np.flip(cube[Sides.back, 2, :])     cube[Sides.front, 0, :] = cube[Sides.bottom, 0, :]     tmp = np.array(cube[Sides.front, 0, :]) def left_counter():       return "L"     cube[Sides.left, :, :] = np.rot90(cube[Sides.left, :, :])      cube[Sides.bottom, 0, :] = tmp     cube[Sides.back, 2, :] = np.flip(cube[Sides.bottom, 0, :])     cube[Sides.top, 0, :] = np.flip(cube[Sides.back, 2, :])     cube[Sides.front, 0, :] = cube[Sides.top, 0, :]     tmp = np.array(cube[Sides.front, 0, :]) def left():       return "R'"     cube[Sides.right, :, :] = np.rot90(cube[Sides.right, :, :])      cube[Sides.bottom, 2, :] = tmp     cube[Sides.back, 0, :] = np.flip(cube[Sides.bottom, 2, :])     cube[Sides.top, 2, :] = np.flip(cube[Sides.back, 0, :])     cube[Sides.front, 2, :] = cube[Sides.top, 2, :]     tmp = np.array(cube[Sides.front, 2, :]) def right_counter():       return "R"     cube[Sides.right, :, :] = np.rot90(cube[Sides.right, :, :], -1)      cube[Sides.top, 2, :] = tmp     cube[Sides.back, 0, :] = np.flip(cube[Sides.top, 2, :])     cube[Sides.bottom, 2, :] = np.flip(cube[Sides.back, 0, :])     cube[Sides.front, 2, :] = cube[Sides.bottom, 2, :]     tmp = np.array(cube[Sides.front, 2, :]) def right():           print(line)             line += cube[Sides.bottom, x, y]         for x in range(0, 3):         line = "   "     for y in range(2, -1, -1):     # bottom          print(line)                 line += cube[side, x, y]             for x in range(0, 3):         for side in [Sides.left, Sides.front, Sides.right, Sides.back]:         line = ""     for y in range(2, -1, -1):     # left, front, right, back          print(line)             line += cube[Sides.top, x, y]         for x in range(0, 3):         line = "   "     for y in range(2, -1, -1):     # top def debug():   #cube[Sides.right, 0, 2] = 'k'  cube[Sides.right, :, :] = 'r' cube[Sides.left, :, :] = 'm' cube[Sides.back, :, :] = 'g' cube[Sides.front, :, :] = 'b' cube[Sides# Creates the cub## Creates the cube in text format  cube = np.empty(shape=(6, 3, 3), dtype='str')       right = 5     left = 4     back = 3     front = 2     top = 1     bottom = 0 class Sides:   import numpy as np ad  
  �
     1       �  �  �  �  �  y  D    �  �  �  �  �  �  �  c  0  �  �  �  �  \  M  L  K  6    
  �  �  �  �  �  �  �  �  �  �  j  7    �  �  �  e  U  T  S  �
  �
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        method_list = [right, right_counter, left, left_counter, up, up_counter, down, down_counter]       return "B'"     cube[Sides.back, :, :] = np.rot90(cube[Sides.back, :, :], -1)      cube[Sides.right, 2, :] = tmp     cube[Sides.bottom, :, 2] = cube[Sides.right, 2, :]     cube[Sides.left, 2, :] = cube[Sides.bottom, :, 2]     cube[Sides.top, :, 2] = cube[Sides.left, 2, :]     tmp = np.array(cube[Sides.top, :, 2]) def back_counter():       return "B"         back_counter()     for number in range(3): def back():       return "F'"         front()     for number in range(3): def front_counter():       return "F"     cube[Sides.front, :, :] = np.rot90(cube[Sides.front, :, :], -1)      cube[Sides.right, 0, :] = tmp     cube[Sides.bottom, :, 0] = cube[Sides.right, 0, :]     cube[Sides.left, 0, :] = cube[Sides.bottom, :, 0]     cube[Sides.top, :, 0] = cube[Sides.left, 0, :]     tmp = np.array(cube[Sides.top, :, 0]) def front():       return "D'"     cube[Sides.bottom, :, :] = np.rot90(cube[Sides.bottom, :, :])      cube[Sides.left, :, 0] = tmp     cube[Sides.back, :, 0] = cube[Sides.left, :, 0]     cube[Sides.right, :, 0] = cube[Sides.back, :, 0]     cube[Sides.front, :, 0] = cube[Sides.right, :, 0]     tmp = np.array(cube[Sides.front, :, 0]) def down_counter():       return "D" ad  �   �     t       �  �  �  �  m  O  N  /  .  -       �  �  �  �  �  �  f  G  5  �  �  �  �  �  �  a  L  .    �  �  �  �  �  {  <     �  �  �  �  �  �  u  I    �
  �
  w
  v
  6
  &
  %
  $
  
  �	  �	  |	  =	  	  	  �  �  �  �  �  �  S    �  �  �  u  e  d  c  Y  -  �  �  �  m  l  ,        	      �  �  �  �  m  [  /  �  �  �  o  n  2  "  !       �  �    J  (  '  �                                                                                                                                                                                                                         cube[Sides.bot                        cube[Sides.bottom, :, :] = np.rot90(cube[Sides.bottom, :, :], -1)      cube[Sides.right, :, 0] = tmp     cube[Sides.back, :, 0] = cube[Sides.right, :, 0]     cube[Sides.left, :, 0] = cube[Sides.back, :, 0]     cube[Sides.front, :, 0] = cube[Sides.left, :, 0]     tmp = np.array(cube[Sides.front, :, 0]) def down():       return "U'"     cube[Sides.top, :, :] = np.rot90(cube[Sides.top, :, :])      cube[Sides.right, :, 0] = tmp     cube[Sides.back, :, 2] = cube[Sides.right, :, 2]     cube[Sides.left, :, 2] = cube[Sides.back, :, 2]     cube[Sides.front, :, 2] = cube[Sides.left, :, 2]     tmp = np.array(cube[Sides.front, :, 0])     time.sleep(2)     print("Moves applied: " + str(x) + "x \n") def randomization():   x = int(input("Wie oft sollen random Moves auf den Würfel ausgeübt werden?"))       def up_counter():       return "U"     cube[Sides.top, :, :] = np.rot90(cube[Sides.top, :, :], -1)      cube[Sides.left, :, 0] = tmp     cube[Sides.back, :, 2] = cube[Sides.left, :, 2]     cube[Sides.right, :, 2] = cube[Sides.back, :, 2]     cube[Sides.front, :, 2] = cube[Sides.right, :, 2]     tmp = np.array(cube[Sides.front, :, 0]) def up():       return "L'"     cube[Sides.left, :, :] = np.rot90(cube[Sides.left, :, :], -1)      cube[Sides.top, 0, :] = tmp     cube[Sides.back, 2, :] = np.flip(cube[Sides.top, 0, :])     cube[Sides.bottom, 0, :] = np.flip(cube[Sides.back, 2, :])     cube[Sides.front, 0, :] = cube[Sides.bottom, 0, :]     tmp = np.array(cube[Sides.front, 0, :]) def left_counter():       return "L"     cube[Sides.left, :, :] = np.rot90(cube[Sides.left, :, :])      cube[Sides.bottom, 0, :] = tmp     cube[Sides.back, 2, :] = np.flip(cube[Sides.bottom, 0, :])     cube[Sides.top, 0, :] = np.flip(cube[Sides.back, 2, :])     cube[Sides.front, 0, :] = cube[Sides.top, 0, :]     tmp = np.array(cube[Sides.front, 0, :]) def left():       return "R'"     cube[Sides.right, :, :] = np.rot90(cube[Sides.right, :, :])      cube[Sides.bottom, 2, :] = tmp     cube[Sides.back, 0, :] = np.flip(cube[Sides.bottom, 2, :])     cube[Sides.top, 2, :] = np.flip(cube[Sides.back, 0, :])     cube[Sides.front, 2, :] = cube[Sides.top, 2, :]     tmp = np.array(cube[Sides.front, 2, :]) def right_counter():       return "R"     cube[Sides.right, :, :] = np.rot90(cube[Sides.right, :, :], -1)      cube[Sides.top, 2, :] = tmp     cube[Sides.back, 0, :] = np.flip(cube[Sides.top, 2, :])     cube[Sides.bottom, 2, :] = np.flip(cube[Sides.back, 0, :])     cube[Sides.front, 2, :] = cube[Sides.bottom, 2, :]     tmp = np.array(cube[Sides.front, 2, :]) def right():           print(line)             line += cube[Sides.bottom, x, y]         for x in range(0, 3):         line = "   "     for y in range(2, -1, -1):     # bottom          print(line)                 line += cube[side, x, y]             for x in range(0, 3):         for side in [Sides.left, Sides.front, Sides.right, Sides.back]:         line = ""     for y in range(2, -1, -1):     # left, front, right, back          print(line)             line += cube[Sides.top, x, y]         for x in range(0, 3):         line = "   "     for y in range(2, -1, -1):     # top def debug():   #cube[Sides.right, 0, 2] = 'k'  cube[Sides.right, :, :] = 'r' cube[Sides.left, :, :] = 'm' cube[Sides.back, :, :] = 'g' cube[Sides.front, :, :] = 'b' cube[Sides.top, :, :] = 'y' cube[Sides.bottom, :, :] = 'w' 