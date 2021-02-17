// Task
// Copmlete the function in the editor, it has one parameter an array, nums.
// Must iterate through the array performing one of the following actions
//  element even multiply by two
// element odd multiple by three
// function then returns the modified array


function modifyArray(nums) {
  let modifiedArray = []
  nums.forEach((element) => {
    // console.log(element)
    if (element % 2 == 0) {
      modifiedArray.push(element * 2)
    }
    else {
      modifiedArray.push(element * 3)
    }
  })
  return modifiedArray
}


function main() {
    a = [1, 2, 3, 4, 5]
    
    console.log(modifyArray(a))
}

main()