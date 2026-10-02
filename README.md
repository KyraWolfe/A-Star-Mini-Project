# A-Star-Mini-Project

# environment:
- I wrote my code using class Environment, this is because I had messed up about a hundred or more lines of code on my VaccuumWorld and did not have the time or the energy to sift through what was worth saving or not so I scrapped all of it
- This code is heavily influenced by the two links I have added below
- I opted to not use the provided starter code as I ended up confusing myself more trying to work out what to do for each method
- I believe this confusion came from it not being similar to code I have written previously
- Due also to this confusion, I spent far to long trying to unconfuse myself and ended up wasting a lot of time and now my project is not as complete as I would like it to be
- I also added my vaccuum_world, even though it is a terrible mess of code, I believe it shows my thought process throughout this project and kind of what my understanding of it was at the time, it is not my final draft but rather the steps leading to what would become the Environment 

# depth-first:
- This is entirely in one method
- I found a website (codeacademy) that had examples of depth first search
- This website helped me out greatly as I could see the code they wrote and could mentally work through to see what each line did
- I do not understand the code completely, but enough to understand what the goal is
- This lack of understanding is not because of a lack of knowledge but rather a lack of brain function due to a medical condition I possess at this time
- The goal of this method is to start at the start spot (row 0, col 0) and check out each neighboring cell to determine what is in it                       
- after each cell is visited, it is marked as such so the system knows it has already been here 
- the code I found only did the search part and had no code to determine if cells needed to not be touched or if they needed to be modified, both of these are necessary for the roomba to work
- I modified the code I found to include if statements to check if there was dirt, if so then that spot would be changed to clean and 2 would be added to the cost, one for the move to the cell and one for the cleaning of said cell
- I also added an if statement to avoid the obstacle cells, the goal of this was to just move on to the next neighbor when it was encountered
- to show what the trip was, each move is printed out in the form of its index, the first number correlating to the row and the second to the column
- after running the function, it should print the cost of the search and what the grid now looks like with all areas marked "d" for dirty to "c" for clean
- this method does not currently work and I am afraid I do not currently have enough function to brain to debug it where it is needed

# a*:  
- I truly had no idea where to even start with this code function as all I knew about it was f = g + h and I wasn't even really sure what each of those letters meant
- I found a website through geeks for geeks that had code to do a complete a* search, but only the search
- like the depth first website, it lacked code for cleaning dirty spots, however it did show me how to check for obstacles and out of bounds
- since I learned that the formula i mentioned previously is about cost, I elected to just stick with the code I found instead of adding 1 to a cost variable I created
- this code takes up the remainder of the methods inside the environment
- the first method is to check if the roomba is still in bounds by seeing if the row goes above 4 or below 0 and the same check is done on col with the same numbers
- the next method is to check for obstacles, which I marked as "#"
- the next method I added in was to check if the area was dirty, I modified the code for obstacles as it seemed to me like they would be very similar, dirty was marked as "d" in the grid I made
- Next method was to check if we were at the end, I assumed the end would be the square right below the start at row 1 col 0
- The method to calculate the estimated cost or h was next, I opted to write out what each meant so that I understood what I was doing better
- I also have a method "path" which keeps track of each index move the roomba makes
-after all these prep methods comes the a* method
- I am only partially understanding the code but my belief is that it also marks which cells have been visited
- after each move, it calculates a cost and adopts the new cost if it is greater than the old one
- after each move, the first things checked are if the roomba is in bounds, not on an obstacle, its dirty status, and if it is the end
- I was unable to run this code to check if it worked as intended but I am going to assume it probably has some bugs that need worked out
- I don't quite understand how the a* search will actually get to the end and touch all available squares without missing any since if the end is right next to the start, it could easily end up there and not touch the rest of the block, if the end is in the opposite corner like row 3 col 3, then it could miss the little section underneath the start

# ida*:
- I did not have enough time to get to this section
- I understand that there is a math formula to get this section to work, but I was unable to really find any code to see that formula in action

# "main" area:
- This is where I created my list of lists called grid4 and had each square designated "c" for clean, "d" for dirty and "#" for an obstacle
- I converted the list of lists to a dictionary for depth first search as it made more sense in my brain in order to run through each item and see what it was
- I did not want to permanently have grid4 be a dictionary as using it in that way with a* made it much more complicated and harder for me to understand
- Since I decided to change the value of the grid whenever it was clean, I also had it put back to its original before the a* method was called on
- I also had the grid be printed after each method to hopefully show how the dirty cells were changed to clean

# project struggles:
- this project had many struggles for me
- The first is spending too long trying to figure out how to make the starter code work instead of just opting to use methods I was familiar with and finding examples online to follow
- the second was having a lot of bad days during the 3 week time frame, the first week I consistently had a high fever, which made figuring out information really hard, the second week I was pretty good but spent too long on the above point, the third I was entering my pmdd window
- the next issue I had was that I have not worked much with python classes in about 3 years, so I kept defaulting back to the syntax of java, c++, and c, I spent many hours debugging errors of me using semicolons, curly brackets, and too many extra parenthesis

# conclusion:
- Overall I believe I did learn more about each of the search methods
- I would not consider my skills mastered but they are definitely greater than when I went into this project
- If I could do things differently, I would probably spend my first week just trying to relearn python classes so I could be more prepared to code, I would also try something different when I first realized that the starter code would not work for me instead of spending extra time working on something that was never going to succeed 
- The last point I need to make is that I didn't ask for help even though it was very clear I needed it, I think part of this is just because I have been very busy the past few weeks but looking back I can see a few hours here and there that I could have asked a question, for upcoming projects of this scale, I am going to make sure that once I realize I need help that I ask for it

# references:
- https://www.geeksforgeeks.org/python/a-search-algorithm-in-python/ 
- https://www.codecademy.com/article/depth-first-search-dfs-algorithm
