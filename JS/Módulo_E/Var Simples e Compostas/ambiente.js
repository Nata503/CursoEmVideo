let num  = [5,8,2,9,3]
num[5] = 6
num.push(8)

// for(let pos = 0;pos < num.length; pos++){
//     console.log(`A posição ${pos} seria ${num[pos]}`)
// }

for(let pos in num){
    console.log(`A posição ${pos} seria ${num[pos]}`)
}

console.log(`O vetor tem ${num.length} posições`)
console.log(`O primeiro valor do vetor é ${num[0]}`)