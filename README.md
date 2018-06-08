# Random Key Generation With graphs

### Overview

This code will create a random key for a application by the follwoing methods.
  - A Graph of letters a-z A-Z 1-9 is created
  - Each node contains two random vertexs weighted 1-9
  - Two points on the graph are randomly selected 
  - Dijkstras is run to generate a key 
  - Profit?
  
### Known issues

This algorithm is a proof of concept and does come with a fair ammount of flaws they are as such
  1. We used pythons basic random class to generate random numbers which by itself is not that random and can be easily hacked
  2. Keys do not have to be a minimum length so you can get a key of length 2 
  3. There is a issue where the start and end point will be the same node causing a error 
  
### Areas of improvement 

Currently the graph takes up a lot of space in memory so creating a more efficent graph is key.  Second repalcing the random library with a better RNG is a must for sequrity.  We also need to create a min key leanth to prevent easy to guess keys.  

### End Notes

This algortim was one of our own creation as far as we can tell, if you end up using this in some capacity, any credit is apprecied.  A more in depth anylisis can be found in the repo, this includes runtimes of code
