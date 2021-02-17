// Task
// The code has a tagged template that passes the area and perimeter of a rectangle to a tag function named sides
// The first argument of a tag function is an array of string literals form the template and the subsequent values are the templates respective expression values
// Complete the function in the editor
//  Finds the intial values of s1 and s2 by plugging in the area and perimeter values into the formula
//  Creates an array consisting of s1 and s2 and sorts it in ascending order
//  Returns the assorted array

function sides(literals, ...expressions) {
  const [a, p] = expressions;
  const root = Math.sqrt((p*p)-(16*a))
  const s1 = (p + root)/4;
  const s2 = (p - root)/4;
  return ([s2, s1]).sort();
}