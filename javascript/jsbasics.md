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
if a variable is named but it has no value. It goes to undefined.

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
It is same for != as well. So !== should be used instead.
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
