'use strict';
class InsertionSort {
  sort(arr){
    for(var i = 0; i < arr.length; i++){
      var val = arr[i],
      newPos = this.getPositionForNewVal(val, arr);
      arr.splice(i,1);
      arr.splice(newPos,0,val);
    }
    return arr;
  }

  getPositionForNewVal(val, arr){
    for( var i = 0; i < arr.length; i++ ){
      if (val <= arr[i]){
        return i;
      }
    }
    return i;
  }
}
