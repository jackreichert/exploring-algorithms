'use strict';
class InsertionSort {
  sort(arr){
    var newArr = [];
    for(var i = 0; i < arr.length; i++){
      newArr = this.insertIntoPlace(newArr, arr[i]);
    }
    return newArr;
  }
  insertIntoPlace(arr, newVal){
    for( var i = 0; i < arr.length; i++){
      if (undefined === typeof arr[i] || arr[i] > newVal){
        arr.splice(i,0,newVal);
        return arr;
      }
    }
    arr.push(newVal);
    return arr;
  }
}
