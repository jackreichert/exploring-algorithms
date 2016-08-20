'use strict';
class InsertionSort {
  insertIntoPlace(arr, val){
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
