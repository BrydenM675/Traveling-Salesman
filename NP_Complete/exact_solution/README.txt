Here is the exact solution to tsp by Bryden Mollenauer
CD into the test directory
you might have to run chmod +x run_test_cases.sh
then run ./run_test_cases.sh

the output for each test will be put in separate txt files

to run the 20 min test
run ./20min.sh

hopefully will run for you but runs out of memory for me

Small Test explenation
The test case is made so there are 5 vertexes and the shortest path is going around the outside of graph think of it
like a pentagon. So the alrogrithm will go through all the subsets of the graph and end up with the shortest path of getting
to vertex A to E is a cost of 10 and then it will add the cost of getting back to A from E which is a cost of 5
retunrning a cost of 15 which is what the test case produced.
