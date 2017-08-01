function numbersOnly(myArray){
  var changeArray = [];
  for (var i = 0; i < myArray.length; i++){
    if (typeof myArray[i] === "number"){
      changeArray += myArray[i];
    }
  }
  return changeArray;
}

var newArray = numbersOnly([1, "apple", -3, "orange", 0.5]);

console.log(newArray);
