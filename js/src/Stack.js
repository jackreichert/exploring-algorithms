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
    if ( 0 === this.getSize() ) {
      throw new Error("StackUnderflow");
    }

    return this.content.splice(this.content.length - 1, 1)[0];
  }

  peek() {
    return this.content[this.content.length - 1 ];
  }
}
