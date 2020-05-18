# Suduko
This repository contains the code for creating and solving sudoku board.
The Suduko Program contains three files:
         ->  checkBox.py
         ->  create_board.py
         ->  myChoice.py
         
 To run the program follow the steps:
     -> Download the zip file.
     
     -> Extract all files in the same folder.
     
     -> Run create_board.py file using a terminal or ide (whichever method is preferred by you).
     
     -> Once the create_board.py file runs it will ask for input.
     
     -> Enter the number of grid to be initially filled in Suduko board.
     
     -> Select any one option from the give two option.
     
     -> If option 1 is selected the Sudoku board will be created automatically with the specified number of grid already filled.
     
     -> If option 2 is selected the user will have to select the grid and the number to input manually to create Sudoku Board.
     
     Note:- Currently the program may take input from terminal only (No GUI is available).
     
     Note:-
         known issues:-
     
             -> Currently the program is under development and may sometimes crash unexpectedly 
             (Especially when the input of Number of known values to insert is high but under allowed range.)
     
             -> Program may also run into an infinite loop if Number of known values to insert is high (until crashed)
             
             ->  Index error may occur sometimes on large input values
             
             -> Unexpected behaviour if Number of known values is not in the permissible range
