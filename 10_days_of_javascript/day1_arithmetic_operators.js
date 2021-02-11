// Task
// Complete getArea function, calculate and return the area of a rectangle having sides length and width
// Complete getPerimeter function, calculate and return the perimater of a rectangle having sides length and width

function getArea(length, width) {
  let area;
  // Write your code here
  area = Number(length) * Number(width)
  
  return area;
}

function getPerimeter(length, width) {
  let perimeter;
  // Write your code here
  perimeter = 2 * (Number(length) + Number(width))
  return perimeter;
}


function main() {
  const length = "3"
  const width = "4.5"
  
  console.log(getArea(length, width));
  console.log(getPerimeter(length, width));
}

main()