var hour = 1;
var min = 45;

if (min == 15)
{
    console.log("The time is quarter past " + hour);
}
else if (min == 30)
{
    console.log("The time is half past " + hour);
}
else if (min == 45)
{
  if (hour != 12){
    console.log("The time is a quarter til " + (hour + 1));
  }
  else
  {
    console.log("The time is a quarter til 1");
  }
}
else if (min <= 29)
{
  console.log("The time is " + min + " minutes past " + hour);
}
else
{
  if (hour != 12)
  {
    console.log("The time is " + min + " minutes til " + (hour + 1));
  }
  else
  {
    console.log("The time is " + min + " minutes til 1")
  }
}
