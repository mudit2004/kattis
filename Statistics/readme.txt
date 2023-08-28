'Research often involves dealing with large quantities of data, and those data are often too massive to examine manually. Statistical descriptions of data can help humans understand their basic properties. Consider a sample of  numbers . Of many statistics that can be computed on , some of the most important are the following:

: the smallest value in 

: the largest value in 

: 

Write a program that will analyze samples of data and report these values for each sample.

Input

The input contains between  and  test cases. Each test case is described by one line of input, which begins with an integer  and is followed by  integers which make up the sample to be analyzed. Each value in the sample will be in the range  to . Input ends at the end of file.

Output

For each case, display Case X:, where X is the case number, followed by the min, max, and range of the sample (in that order). Follow the format of the sample output.

Sample Input 1	Sample Output 1
2 4 10
9 2 5 6 4 5 9 2 1 4
7 6 10 1 2 5 10 9
1 9
Case 1: 4 10 6
Case 2: 1 9 8
Case 3: 1 10 9
Case 4: 9 9 0
'
