// Task
// Complete the getSecondLargest function, it has one parameter an array nums of n integers
// The function must find a return the second largest number in nums

function getSecondLargest(nums) {
  // Complete the function
  // remove duplicates from the array
  const uniq = ([...new Set(nums)]) 
  const sorted = uniq.sort(function(a,b){return b - a})
  const secondLargest = sorted[1]
  return secondLargest
}

function main() {
  const nums = [2, 3, 6, 6, 5]
  // const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  
  console.log(getSecondLargest(nums));
}

main()