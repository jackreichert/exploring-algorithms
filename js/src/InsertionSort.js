'use strict';
class InsertionSort {
  sort(arr){
    var newArr = [];
    for(var i = 0; i < arr.length; i++){
      newArr = this.insertIntoPlace(arr[i], newArr);
    }
    return newArr;
  }

  insertIntoPlace(val, arr){
    for( var i = 0; i < arr.length; i++ ){
      if (val < arr[i]){
        arr.splice(i,0,val);
        return arr;
      }
    }
    arr.push(val);
    return arr;
  }
}
