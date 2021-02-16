// Task
// Complete the function in the editor
// It has one parameter: an array a of objects
// Each object in the array has two integer properties denoted by x and y
// This function must return a count of all such objects o in array a that statisfy x = y

function getCount(objects) {
  let total_count = 0
  for (const [key, value] of Object.entries(objects)) {
      if (value['x'] == value['y']) {
          total_count += 1
      }
  }       
  return total_count
}