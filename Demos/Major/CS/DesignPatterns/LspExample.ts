class Rectangle {
  constructor(private width: number, private length: number = 10) {}

  public setWidth(width: number) {
    this.width = width;
  }

  public setLength(length: number) {
    this.length = length;
  }

  public getArea() {
    return this.width * this.length;
  }
}

class Square extends Rectangle {
  constructor(side: number) {
    super(side, side);
  }

  public setWidth(width: number) {
    // A square must maintain equal sides
    super.setWidth(width);
    super.setLength(width);
  }

  public setLength(length: number) {
    super.setWidth(length);
    super.setLength(length);
  }
}

// const rect: Rectangle = new Rectangle(10); // Can be either a Rectangle or a Square
// rect.setWidth(20);
// if(rect.getArea() > 300) {
//   console.log('It is big!')
// }else {
//   console.log('It is small!' )
// } // 200

const rect: Rectangle = new Rectangle(10); // Can be either a Rectangle or a Square
rect.setWidth(20);
if (rect.getArea() > 300) {
  console.log("It is big!");
} else {
  console.log("It is small!");
} // 400
