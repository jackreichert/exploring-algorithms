class LinkedList {
  constructor() {
    this._length = 0;
    this.head = this.newNode();
  }

  newNode(){
    return {
      value: null,
      next: null
    };
  }

  getNext(){
    return null;
  }

  getLength(){
    return this._length;
  }

  add(value){
    var current = this.findTail();
    current.value = value;
    current.next = this.newNode();
    this._length++;
  }

  findTail(){
    return this.searchNodeAt(this._length);
  }

  searchNodeAt(position){
    var current = this.head,
    i = 0;
    while( null !== current.next && i < position ) {
      current = current.next;
      i++;
    }
    return current;
  }

  searchValueAt(position){
    return this.searchNodeAt(position).value;
  }

  getNodeAfterNext(node){
    return node.next.next;
  }

  removeNodeAt(position){
    if (0 === position){
      this.head = this.head.next;
    } else {
      var nodeBeforePositionToDelete = this.searchNodeAt(position-1),
      nodeAfterPositionToDelete = this.getNodeAfterNext(nodeBeforePositionToDelete);
      nodeBeforePositionToDelete.next = nodeAfterPositionToDelete;
    }
    this._length--;
  }

};
