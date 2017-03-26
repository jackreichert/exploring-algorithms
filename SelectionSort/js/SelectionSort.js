'use strict';

class SelectionSort {
  findIndexOfLowest(numberList){
    var lowest = 0;
    numberList.forEach((val,i) => {
      lowest = numberList[lowest] > val ? i : lowest;
    });
    return lowest;
  }

  swap(numberList, from, to) {
    var temp = numberList[to];
    numberList[to] = numberList[from];
    numberList[from] = temp;
    return numberList;
  }

  sort(numberList) {
    numberList.forEach((val, i) => {
      var lowest = i + this.findIndexOfLowest(numberList.slice(i));
      numberList = this.swap(numberList, i , lowest);
    });

    return numberList;
  }
}
