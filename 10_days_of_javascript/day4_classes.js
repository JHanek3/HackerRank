// Task
// Create a polygon class that has the following properties
// A constructor that takes an array of integer values describing the lengths of the polygon's sides
// A perimeter method that retunrs the polygon's perimeter

class Polygon {
  constructor(sides = []) {
    this.sides = sides
  }
  //Getters, no ndeed for getters because its a function call at the console.log
  // get perimeter() {
  //   return this.calcPerimeter()
  // }

  //Methods
  perimeter() {
    let perimeter = 0
    for (var i = 0; i < this.sides.length; i++) {
      perimeter += this.sides[i]
    }
    return perimeter
  }
}

const rectangle = new Polygon([10, 20, 10, 20]);
const square = new Polygon([10, 10, 10, 10]);
const pentagon = new Polygon([10, 20, 30, 40, 43]);
let triangle = new Polygon([3, 4, 5]);

console.log(rectangle.perimeter());
console.log(square.perimeter());
console.log(pentagon.perimeter());
console.log(triangle.perimeter());