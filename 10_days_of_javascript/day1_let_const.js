// Task
// Declare a constant variable PI, and assign it the value Math.PI
// Read a number r, denoting the radious of a circle from stdin
// Use PI and r to calculate the area and perimeter of a circle having radius r
// Print area as the first line of output and print perimeter as the second line of output

function main() {
  // Write your code here. Read input using 'readLine()' and print output using 'console.log()'.
  const PI = Math.PI
  console.log(PI)
  const r = readLine()
  // r = "2.6"

  
  // Print the area of the circle:
  console.log(PI * (Number(r) * Number(r)))
  
  // Print the perimeter of the circle:
  console.log(2 * PI * Number(r))

  try {    
      // Attempt to redefine the value of constant variable PI
      PI = 0;
      // Attempt to print the value of PI
      console.log(PI);
  } catch(error) {
      console.error("You correctly declared 'PI' as a constant.");
  }
}

main()