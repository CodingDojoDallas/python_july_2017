var numQrts = 25;

function quarters(numQrts){
  var winningNum = Math.trunc(Math.random() * 100);
  //console.log("*****Winning Number:  " + winningNum + "*****");

  for (var i = numQrts; i > 0; i--){
    var lotteryNum = Math.trunc(Math.random() * 100);
    if (winningNum == lotteryNum){
      var winnings = Math.trunc((Math.random() * 50)+50);
      var payOut = i + winnings;
      console.log("You won " + winnings + " quarters.  You now have " + payOut + " quarters.");
      return payOut;
    }
  }
  console.log("Out of quarters.  You lose.")
}

quarters(numQrts);
