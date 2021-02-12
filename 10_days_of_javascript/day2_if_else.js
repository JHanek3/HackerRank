// Task
// Complete the getGrade(score) function in the editor. It has one parameter, score, denoting the number of point Julia earned on an exam
// It must return the letter corresponding to her grade

function getGrade(score) {
  let grade;
  // Write your code here
  score = Number(score)
  if (30 >= score && score > 25) {
    grade = "A"
  }
  else if (25 >= score && score > 20) {
    grade = "B"
  }
  else if (20 >= score && score > 15) {
    grade = "C"
  }
  else if (15 >= score && score > 10) {
    grade = "D"
  }
  else if (10 >= score && score > 5) {
    grade = "E"
  }
  else {
    grade = "F"
  }
  
  return grade;
}

function main() {
  console.log(getGrade("11"));
}

main()