/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop
var x=1;
while (x<6) {
  console.log("Hello World!");
  x=x+1;
}

// For Loop
for(var i=1; i<6; i++)
{
  console.log("Hello World!");
}



/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop
var x=1;
while(x<26)
{
  if(x%2 === 1)
  {
    console.log(x);
  }
  x=x+1;
}

// METHOD TWO
// For Loop
for(var x=1;x<26;x=x+2)
{
  console.log(x);
}
