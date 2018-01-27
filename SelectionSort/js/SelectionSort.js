'use strict';

class SelectionSort {
	findIndexOfLowest(numberList) {
		var lowest = 0;
		numberList.forEach((val, i) => {
            lowest = val < numberList[lowest] ? i : lowest;
        });
		return lowest;
	}

    swapFromTo(numberList, from, to) {
        let tempFrom = numberList[from];
        numberList[from] = numberList[to];
        numberList[to] = tempFrom;
        return numberList;
    }

    sort(numberList) {
        numberList.forEach( (val,i) => {
            let indexOfLowest = i + this.findIndexOfLowest(numberList.slice(i));
            numberList = this.swapFromTo(numberList, i, indexOfLowest);
        });
        return numberList;
    }
}
