-this section of code is for checking 4 consecutive diagonal counters in a game of connect 4

-to do this, i surround the board with empty columns on the left and right side of the board
-then, i check the diagonal starting from the leftmost diagonal e.g [0,0] [1,1] [2,2]
-after a diagonal is checked, i shift to the next diagonal e.g. [0,1] [1,2] [2,3]

-a better implementation could be to rotate the board such that the diagonals become horizontals or verticals
-this could allow me to reuse previous code which checks the horiztals and verticals for 4 consecutive counters