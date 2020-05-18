# Implementation
I implemented my quest reward maximization program by first reading all available 
quests from a CSV file.  This way my program can accept any list of quests, as long 
as the quests are correctly formatted in a CSV file, which can be seen in example.csv. 
Once I have all the quests, I sort them from highest to lowest reward, so that I can 
start by adding the highest reward quests to my quest log to maximize 
reward.  Then I loop through the other quests and check if the current quest can be added to 
the log by also looping through the quests currently in the log and making sure that 
none of the quests overlap.  Once I've added all the quests I can to the log, I check 
to see if the current log I have provides a greater reward than other quest logs.  If 
it does, then I update the maximum reward and the required quests to achieve that reward. 
Now I try different combinations to find other maximum reward combinations and once the loop 
on lines 49-67 is finished I print out the maximum reward and sort the maximum reward 
list so that the quests can be displayed in the order that they should be completed.

# Modularity
My solution would be successful with other quest boards because they would just need 
to be correctly formatted in a CSV file then my program can read the quests and provide 
the maximum reward and the order to complete the quests.

# Efficiency
The larger the given quest board is the less efficient my solution is, because I rely on 
for loops to create different combinations of quests to maximize the reward.  To
be exact, the worst-case time complexity of my program is O(3mn<sup>2</sup>) given that n is the 
total number of quests, m is the number of quests being considered for maximizing reward, 
and the basic operation is comparisons.
