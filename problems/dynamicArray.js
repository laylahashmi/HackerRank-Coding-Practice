/*
 * Complete the 'dynamicArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

function dynamicArray(n, queries) {
    let arr = [], lastAnswer = 0, answers = [];
   for(let j = 0; j < n; j++){
       arr.push([])
   }
   for(let i = 0; i < queries.length; i++){
       const query = queries[i];
       const [queryType, x, y] = query
       const idx = (x ^ lastAnswer) % n;
       if(queryType === 1){
           arr[idx].push(y)
       }else if(queryType === 2){
           lastAnswer = arr[idx][y % arr[idx].length]
           answers.push(lastAnswer)
       }
   }
   return answers

}
