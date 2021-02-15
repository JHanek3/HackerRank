// Task
// Complete the isPositive functino below
// It has one integer parameter, a. If the value of a is positive, it must return the string YES
// Otherwise, it must throw an error according the following rules
// IF a is 0, throw an Error with message = Zero Error
// If a is negative, throw an Error with message = Negative Error

function isPositive(a) {
  if (a > 0) {
    return "YES"
  }
  else if (a == 0) {
    throw new Error("Zero Error")
  }
  else {
    throw new Error("Negative Error")
  }
}


function main() {
  const n = -1

  try {
    console.log(isPositive(n))
  } catch (e) {
    console.log(e.message)
  }
}
main()