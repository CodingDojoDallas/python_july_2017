var daysUntilMyBirthday = 0;

function birthdayCountdown(daysUntilMyBirthday){
  if (daysUntilMyBirthday === 0){
    console.log("Happy Birthday!!!");
  }
  else if(daysUntilMyBirthday <= 10){
    console.log(daysUntilMyBirthday + " days until my birthday!  Almost there!!!  Can't wait!!!");
  }
  else if(daysUntilMyBirthday <= 30){
    console.log(daysUntilMyBirthday + " days until my birthday.  It's getting closer!");
  }
  else if(daysUntilMyBirthday <= 45){
    console.log(daysUntilMyBirthday + " days until my birthday.  Not too long to go!");
  }
  else{
    console.log(daysUntilMyBirthday + " days until my birthday.  Such a long time... :(");
  }
}

birthdayCountdown(daysUntilMyBirthday);
