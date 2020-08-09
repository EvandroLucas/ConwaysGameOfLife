# ConwaysGameOfLife
My own implementation of Conway's Game Of Life using Numpy, PyGame and PyOpenGL. 

This script will render a grid on a new window, and allow you to draw on the screen while it's paused. To be honest, you can draw on the screen even when it is running, but the inserted cells will die before you can even see them. 

You'll probally need to `pip install` those 3 libraris in order for it to work. 

Once everything is set up, just run: 

      python2 GOL.py 50 50
  
To start the game with a 50x50 grid. The game will start paused and blank. To add stuff to it, see the commands below: 

- Press `space` to play/pause the game
- Press or hold `left click` to insert live cells, and `right click` to kill living cells. 
    - Do it while paused so you can see what's going on
- Press `R` to fill the whole grid randomly
- Press `del` to erase the whole grid

![Game running](https://github.com/EvandroLucas/ConwaysGameOfLife/blob/master/Prints/Screenshot%20from%202020-08-09%2012-27-35.png)

![You can draw on canvas](https://github.com/EvandroLucas/ConwaysGameOfLife/blob/master/Prints/Screenshot%20from%202020-08-09%2012-33-21.png)



