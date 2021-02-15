// Task
// Complete the reverseString function, it has one parameter s
// Try to reverse the string s using the split, reverse and join methods
// If an exception is throw, catch it and print the contents of the exception's message on a new line
// Print s on a new line. If no expcetion was thrown then this should be the reversed string, if an exceptions was thrown,
// this should be the original string

function reverseString(s) {
  try {
    s = s.split("")
    s = s.reverse()
    s = s.join("")
  } catch (e) {
    console.log(e.message)

  } finally {
    console.log(s)
  }
}

function main() {
  const s = Number(1234)
  
  reverseString(s);
}

main()