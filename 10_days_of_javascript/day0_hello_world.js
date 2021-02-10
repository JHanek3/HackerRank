// Task
// A greeting function is provided for you in the editor below, one parameter parameterVariable.
// Perform the following tasks to complete this challenge:
// Use console.log() to print Hello, World! on a new line in the console
// Use console.log() to print the contents of parameterVariable

/**
*   A line of code that prints "Hello, World!" on a new line is provided in the editor. 
*   Write a second line of code that prints the contents of 'parameterVariable' on a new line.
*
*	Parameter:
*   parameterVariable - A string of text.
**/

function greeting(parameterVariable) {
    // This line prints 'Hello, World!' to the console:
    console.log('Hello, World!');

    // Write a line of code that prints parameterVariable to stdout using console.log:
    console.log(parameterVariable)
    
}

function main() {
  const parameterVariable = "Welcome to 10 Days of JavaScript!";
  
  greeting(parameterVariable);
}

main()


