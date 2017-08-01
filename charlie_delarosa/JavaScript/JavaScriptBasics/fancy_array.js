var myArray = ['James', 'Jill', 'Jane', 'Jack'];


function fancyArray(myArray){
  for (i = 0; i < myArray.length; i++){
    console.log(i + " -> " + myArray[i]);
  }
}

fancyArray(myArray);
