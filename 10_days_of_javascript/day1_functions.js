// Task
// Implement a function named factorial that has one parameter: an integer n. It must return the value of n!

function factorial(n) {
  if (n === 0)
  return 1
  else {
    return n * factorial( n - 1)
  }
}

function main() {
  console.log(factorial(4));
}

main()