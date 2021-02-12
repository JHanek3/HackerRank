// Task
// Complete the getLetter(s) function in the editor. It has one parameter, string s, consisting of lowercase letters
// Using a switch statement have it return A, B, C, D on the following criteria:

function getLetter(s) {
  let letter;
  switch(true) {
    case /[aeiou]/.test(s[0]) :
      letter = "A"
      break;
    case /[bcdfg]/.test(s[0]) :
      letter = "B"
      break;
    case /[hjklm]/.test(s[0]) :
      letter = "C"
      break;
    case /[npqrstvwxyz]/.test(s[0]) :
      letter = "D"
      break;
  }
  
  return letter;
}

function main() {
  const s = "nhbadfgt";
  
  console.log(getLetter(s));
}

main()