'
The construction worker previously known as Lars has many bricks of height  and different lengths, and he is now trying to build a wall of width  and height . Since the construction worker previously known as Lars knows that the subset sum problem is -hard, he does not try to optimize the placement but he just lays the bricks in the order they are in his pile and hopes for the best. First he places the bricks in the first layer, left to right; after the first layer is complete he moves to the second layer and completes it, and so on. He only lays bricks horizontally, without rotating them. If at some point he cannot place a brick and has to leave a layer incomplete, then he gets annoyed and leaves. It does not matter if he has bricks left over after he finishes.

Yesterday the construction worker previously known as Lars got really annoyed when he realized that he could not complete the wall only at the last layer, so he tore it down and asked you for help. Can you tell whether the construction worker previously known as Lars will complete the wall with the new pile of bricks he has today?

Input

The first line contains three integers , ,  (, , ), the height of the wall, the width of the wall, and the number of bricks respectively. The second line contains  integers  (), the length of each brick.

Output

Output YES if the construction worker previously known as Lars will complete the wall, and NO otherwise.

Sample Input 1	Sample Output 1
2 10 7
5 5 5 5 5 5 5
YES
Sample Input 2	Sample Output 2
2 10 7
5 5 5 3 5 2 2
NO
'
