// Task
// We define S to be a sequence of distinct sequential integers from 1 to n S = {1, 2, 3, ...n}
// Know the maximum bitwise and value of any two integers, a and b, where a < b in sequence S that is also less than given integer k
// Complete the function in the editor so that given n and k return the maximum a & b < k

function getMaxLessThanK(n, k) {
  let max = 0;
  for (let b = n; b > 0; b--) {
      for (let a = b-1; a > 0; a--) {
          if ((a & b) < k && (a & b) > max){
              max = (a&b);
          }
      }
  }
  return max;
}

function main() {    
  console.log(getMaxLessThanK(5, 2));
}

main()