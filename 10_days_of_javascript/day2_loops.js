// Task
// Complete the vowelsAndConsonants function in the editor below, it has one parameter a string s, consisiting of lower case english alphabetical letters
// First print each vowel in s on a new line
// Second, print each consonant in s on a new line in the same order as appeared in s

function vowelsAndConsonants(s) {
    for (let i = 0; i < s.length; i++) {
      if (/[aeiou]/.test(s[i])) {
        console.log(s[i])
      }
    }
    for (let i = 0; i < s.length; i++) {
      if (!/[aeiou]/.test(s[i])) {
        console.log(s[i])
      }
    }
}


function main() {
    const s = "javascriptloops";
    
    vowelsAndConsonants(s);
}
main()