'use strict';

class MergeSort {
  sort(listToSort) {
    if (1 < listToSort.length){
      var mid = this.findMiddle(listToSort),
        leftHalf = this.sort(listToSort.slice(0,mid)),
        rightHalf = this.sort(listToSort.slice(mid));
        listToSort = this.merge(leftHalf, rightHalf);
    }

    return listToSort;
  }

  merge(leftHalf, rightHalf) {
    var i=0,j=0,k=0,
      leftHalfLen = Array.isArray(leftHalf) ? leftHalf.length : 1,
      rightHalfLen = Array.isArray(rightHalf) ? rightHalf.length : 1,
      fullListLength = leftHalf.length + rightHalf.length,
      mergedList = [];

    while( k < fullListLength) {
      if (leftHalf[i] < rightHalf[j]) {
        mergedList.push(leftHalf[i]);
        i++;
      } else if(rightHalf[j] <= leftHalf[i]) {
        mergedList.push(rightHalf[j]);
        j++;
      }

      k++;
    }

    while (i < leftHalf.length) {
      mergedList.push(leftHalf[i]);
      i++;
      k++;
    }

    while (j < rightHalf.length) {
      mergedList.push(rightHalf[j]);
      j++;
      k++;
    }

    return mergedList;
  }

  findMiddle(listToSort) {
    return Math.ceil(listToSort.length/2);
  }
}
