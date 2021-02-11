// Task
// Convert secondInteger to an integer, then sum it with firstInteger and print the result on a new line using console.log
// Convert secondDecimal to a floating-point number, then sum it with first Decimal and print the result using console.log
// Print the concatenation of firstString and secondString on a new line using console.log

function performOperation(secondInteger, secondDecimal, secondString) {
  // Declare a variable named 'firstInteger' and initialize with integer value 4.
  const firstInteger = 4;
  
  // Declare a variable named 'firstDecimal' and initialize with floating-point value 4.0.
  const firstDecimal = 4.0;
  
  // Declare a variable named 'firstString' and initialize with the string "HackerRank".
  const firstString = 'HackerRank ';

  console.log(Number(secondInteger) + firstInteger)
  console.log(firstDecimal + parseFloat(secondDecimal))
  console.log(firstString + secondString)
  
}

function main() {
  const secondInteger = "12"
  const secondDecimal = "4.32"
  const secondString = "is the best place to learn and practice coding!"
  performOperation(secondInteger, secondDecimal, secondString)

}
main()

// performOperation(12, "4.32", "is the best place to learn and practice coding!")
