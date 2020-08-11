# ConwaysGameOfLife
My own implementation of Conway's Game Of Life using Numpy, PyGame and PyOpenGL. 

This script will render a grid on a new window, and allow you to draw on the screen while it's paused. To be honest, you can draw on the screen even when it is running, but the inserted cells will die before you can even see them. 

You'll probally need to `pip install` those 3 libraris in order for it to work. 

Once everything is set up, just run: 

      python3 GOL.py 50 50
  
To start the game with a 50x50 grid. Currently, the maximum number of tiles allowed is 80x80. 
The game will start paused and blank. To add stuff to it, see the commands below: 

- Press `space` to play/pause the game
- Press or hold `left click` to insert live cells, and `right click` to kill living cells. 
    - Do it while paused so you can see what's going on
- Press `R` to fill the whole grid randomly
- Press `del` to erase the whole grid

You can also add "radiation" on yout canvas. This is usefull so you can keep your Game Of Life running for much longer times before the system gets to equilibrium. To do this, just add an integer right after all the previous parameters, like this: 

      python3 GOL.py 50 50 1
     
This will make some random live cells to pop out on screen. The larger this number is, the more live cells will randomly emerge from the void. Currently we support any number in a range of 1 to 10000. 

![Game running](https://github.com/EvandroLucas/ConwaysGameOfLife/blob/master/Prints/Screenshot%20from%202020-08-09%2012-27-35.png)

![You can draw on canvas](https://github.com/EvandroLucas/ConwaysGameOfLife/blob/master/Prints/Screenshot%20from%202020-08-09%2012-33-21.png)



