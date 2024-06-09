var firstName = prompt("Enter your First Name");
var lastName = prompt("Enter your Last Name");
var age = prompt("Enter your Age");
var tall=prompt("Please enter your height (in cms)");
var pet = prompt("Enter your Pet's Name");
alert("Thank you for the information!");

var first=null;
var last=null;
var agenum=null;
var height=null;
var petName=null;

if(firstName[0] === lastName[0])
{
  first = true;
  last =true;
}

if(age > 20 && age < 30)
{
  var agenum = true;
}

if(tall >= 170)
{
  var tall = true;
}

var petLength = pet.length;
if(pet[petLength - 1] === "y" )
{
  var petName = true;
}

if((first ==true) && (last ==true) && (agenum ==true) && (tall ==true) && (petName ==true))
{
  console.log("Welcome Comrade! You've passed the Spy Test");
}
else {
  console.log("You have no business here!");
}
