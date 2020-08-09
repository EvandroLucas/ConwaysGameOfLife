# ConwaysGameOfLife
My own implementation of Conway's Game Of Life using Numpy, PyGame and PyOpenGL. 
This script will draw a grid on a new window, and allow you to draw on the screen while it's paused. To be honest, you can draw on the screen even when it is running, but the inserted cells will die before you can even see them. 

You'll probally need to `pip install` those 3 libraris in order for it to work. 

Once everything is set up, just run: 

  python2 main.py 50 50
  
To start the game with a 50x50 grid. 
The game will start paused, so you can draw on the grid and them play it. 
- Use `space` to play/pause
- Use `left click` to insert live cells, and `right click` to kill living cells. 
- Use `R` to fill the whole grid randomly
- User `del` to erase the whole grid
