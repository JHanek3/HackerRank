// Task
// Given a date string, in the format MM/DD/YYYY, find and return the day name for that date
// Example Output: Monday


function getDayName(dateString) {
  let date = new Date(dateString)
  let dayNumber = date.getDay()
  let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  // Write your code here
  
  return days[dayNumber];
}

function main() { 
  console.log(getDayName("10/11/2009"));
}

main()