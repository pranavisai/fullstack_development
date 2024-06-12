alert("Hello World!") -> this is the function used to create alerts. Here is the example for Hello World!

// -> This is used for comment.

Basic data types:
1. integers
2. float
3. negative number and floats
All of these types are used as numbers.

Strings: They are wrapped in quotes. "10", "Hello World"
Concatenate strings together using +.
".length" -> This is used to calculate the length. space is also counted.
\n -> is used to start a new line.
\t -> is used to give a tab.
\"...." -> is used to quote a word.
"hello"-> the first letter starts at 0 like an array. even spaces are counted.

Booleans: true, false (they should be in lowercase)
undefined and null also exist.

clear() -> to clear the console.
JS can do addition(+), multiplication(*), substraction(-), division (/). This does division correction and not mod.

2**4 -> This is for square. Here the answer is 16.

15%14 is 1. This % is the mod function.

Javascript uses camel case (bankAccount for example.)
setting a variable:
var bankAccount = 100;
same if also want to initialize strings.
if a variable is named but it has no value. It goes undefined.

prompt()-> is used to ask for input.
console.log() -> is for showing output in the console.

var age = prompt("enter input")
This will take the input and store it in the variable age.

Connecting JS to HTML file.
under the title tag use and provide the name of the script.
<script src = "myscript.js"></script>

##Operators:
>, <, >=, >=, == (works even for strings),
js takes "2" == 2 (string equals number as true), hence we need to add one more =. "2" === 2 will be false.
It is the same for != as well. So !== should be used instead.
true == 1 is true.
true === 1 is false. Similar for 0 and false.
null == undefined is true. so use ===.
NaN == NaN is false.

##Logical Operators:
And operator -> &&
OR operator -> ||
NOT -> !

##Control Flow:

if (condition)
{//execute
}
else if {
//execute
}
else {
//execute
}

##While Loop:
while (condition)
{
//execute code.
}

##For Loop:
JS has three types of for loops:
1. For
2. For/In
3. For/Out

for(statement1;statement2;statement3)
{
//execute code
}

##Functions:
function name(parameter 1, parameter 2){
//execute code
}
when calling the function if you do not give any parameters then it will take the parameters as undefined.

function name(parameter 1 = "Joe"){
//execute code
}
This will assign Joe as default if no value is given as input.

function name(parameter 1, parameter 2){
//execute code
return;
}
This will be a local scope of the function.

To have global scope:
var v = "Joe";
var name = "Bin"
function fun(name){
console.log(v);
var name = "Pillar";
console.log(name);
}
fun();

Here first it will check locally if the v value is available and if not then it will check for the global scope and give the output as Joe and Pillar. 

when given the command console.log(name); outside the function. The output will be Joe Pillar Bin as the name is taken from the global value.

##arrays
syntax: var array = [1, 2, 3]
The array index starts from 0.
we can change the value by doing: array[2]= 4. This will change the value of 3 to 4.
An array is mutable -> That means that we give an index and reassign.
JS array can take mixed data types.
Push and pop methods are used to add and remove elements from array.
example:
var number = array.pop(). This will give out 3 and we will only have the array as [1,2]
array.push(4) will add item to array and we will have the answer as [1,2,4].
we can have nested arrays like [[1,2,3], [4,5,6]].
we can have for loop the normal way to iterate or we can use this way:
for (number of array){
console.log(number);
}
This will give the output as:
1
2
4

if you want to give each element of the array as an alert on the website. Then the code is 
for (number of array){
alert(number);
}
The below code is exactly similar to the above one:
arr.forEach(alert);

We can use this in this way as well:
We have a function as 
saySomething(name){
console.log(name+ " is awesome!");
}
var topics= ["python", "django", "science"]
topics.forEach(saySomething)

then the answer will be:
python is awesome
django is awesome
science is awesome

