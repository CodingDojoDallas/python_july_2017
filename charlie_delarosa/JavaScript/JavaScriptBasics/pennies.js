var baseAmount = 0.01;

function doubleYourMoney(baseAmount){
  var newAmount = baseAmount;
  for (var i = 1; i <=30; i++){
    newAmount *= 2;
  }
  return newAmount;
}

doubleYourMoney(baseAmount);
