arr = [1,2,3,4]
arrr = [1,2,3,4]
arr.unshift(0)
console.log(arr[3]-1)

//insert at first
for (let i = arr.length -1; i <= 0; i--){
     arr[i] = arr[i-1]
     console.log(arr)
}
arr[0] = -1
////leteting at first
for (let i = 0; i < arrr.length; i++){
    arrr[i] = arrr[i+1]
    console.log(arrr)
}
