// Task
// Complete the function below, it has two parameters a and b
// It must return an object modeling a rectangle that has the following properties
// length = a
// width = b
// perimeter = 2 * (a + b)
//area = a * b

class Rectangle {
  constructor(length, width) {
    this.length = length;
    this.width = width;
  }

  // Getters
  get perimeter() {
    return this.calcPerimeter()
  }

  get area() {
    return this.calcArea()
  }

  //Methods
  calcPerimeter() {
    return 2 * (this.length + this.width) 
  }
  calcArea() {
    return this.length * this.width
  }
}

function main() {
  const a = 4
  const b = 5
  
  const rec = new Rectangle(a, b);
  
  console.log(rec.length);
  console.log(rec.width);
  console.log(rec.perimeter);
  console.log(rec.area);
}

main()