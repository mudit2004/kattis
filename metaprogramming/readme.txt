'
EIGER is a brand-new, made-up computer language. It’s very exciting, and very simple! EIGER only allows the programmer to do two things: define a name for an integer, and compare two names. Write a metaprogram – a program which can simulate the EIGER language.

Input

Input consists of one command per line, up to  commands, ending at end of file. A definition command has the form define i x, where i is an integer in the range  1and x is a string of up to lowercase alphabet characters (a–z). A comparison command has the form eval x y z, where x and z are strings of the same format as in definitions, and y is one of , , or .

Output

For each definition, use the string as a label for the given integer, but don’t output anything. Redefinitions are allowed. For each comparison, state whether it is true or false, depending on the current definitions. If the result is not known, output ‘undefined’.

Sample Input 1	Sample Output 1
define 5 hellothere
define 6 goodbye
eval hellothere < goodbye
eval hellothere > goodbye
eval hellothere = goodbye
eval hellothere = hi
define 5 hi
eval hellothere = hi
define 6 hi
eval hellothere = hi
true
false
false
undefined
true
false

'
