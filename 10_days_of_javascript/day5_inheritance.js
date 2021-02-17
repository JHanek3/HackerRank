// Task
// The implementation for a rectangle class is provided
// Add an area method to Rectangle's prototype
// Create a square class that statisfies
//  it is a subclass of Rectangle
//  it contains and constructor and no other methods
//  it can use the Recatangle class area methods to print the area of a square object

class Rectangle {
  constructor(w, h) {
      this.w = w;
      this.h = h;
  }
  // Write the area method
  area() {
    return this.w * this.h
  }
}

class Square extends Rectangle {
  constructor(w) {
    super(w)
    this.h = w
  }
}


const rec = new Rectangle(3, 4);
const sqr = new Square(3);

console.log(rec.area());
console.log(sqr.area());
