// Task
// Complete the function that matches an string that
//   starts with the prefix Mr. Mrs. Ms. Dr. or Er.
//  The remainder of the string consists of one or more upper and or lowercase english letters


function regexVar() {
  /*
   * Declare a RegExp object variable named 're'
   * It must match a string that starts with 'Mr.', 'Mrs.', 'Ms.', 'Dr.', or 'Er.', 
   * followed by one or more letters.
   */
  let re = /^(Mr|Mrs|Ms|Dr|Er)(\.)([a-zA-Z])+$/
  /*
   * Do not remove the return statement
   */
  return re;
}
