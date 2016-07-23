/** The Stack Kata **/

class Stack {
  constructor() {
    this.content = [];
  }

  getSize() {
    return this.content.length;
  }

  isEmpty() {
    return 0 === this.getSize();
  }

  push( variable ) {
    this.content[this.content.length] = variable;
  }

  pop() {
    if ( this.isEmpty() ) {
      throw new Error("StackUnderflow");
    }

    return this.content.splice(this.content.length - 1, 1)[0];
  }

  top() {
    if (this.isEmpty()){
      throw new Error("Empty");
    }
    return this.content[this.content.length - 1];
  }

  find(value){
    for( var i = this.getSize() - 1; i >= 0; i-- ){
      if( value ===  this.content[i]){
        return (this.getSize()-1)-i;
      }
    }
    return null;
  }
}
