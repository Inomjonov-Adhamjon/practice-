// TASK G:

// Yagona parametrga ega function tuzing.
// Va bu function parametr orqalik integer ma'lumot turlariga ega bo'lgan bir arrayni qabul qilsin.
// Ushbu function bizga arrayning tarkibidagi birinchi eng katta qiymatning indeksini qaytarsin.

function getHighestIndex(num) {
    let stored = num[0]
    let index = 0

    for (let i = 0; i < num.length; i++) {
        if (num[i] > stored) {
            stored = num[i]
            index = i
        }
    }
    return {
        highestIndex: index,
        highestNumber: stored
    }
}

console.log(getHighestIndex([5, 21, 12, 21, 8]))




// TASK F:

// Yagona string argumentga ega findDoublers nomli function tuzing
// Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
// true yokida false natija qaytarsin.

// function findDoubles(word) {
//     for (let i = 0; i < word.length; i++) {
//         for (let j = 0; j < word.length; j++) {
//             if (word[i] === word[j] && i !== j) {    // harflar bir xil va ularning indexlari har xil
//                 return true                          // bolsa true qaytaradi   
//             }
//         }
//     }
//     return false
// };
// console.log(findDoubles("hello"));
// console.log(findDoubles("Mit"));




// TASK E

// Shunday function tuzing, u bitta string argumentni 
// qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"


// yechim:
// split("") stringni arrayga individual charachterlarga ajratadi
// reverse() ajratilgan value ni teskari qiladi 
// join("") esa teskari qilingan individual stringlarni 
// qaytadan bir string ga birlashtiradi.

// function getReverse(a) {
//     return a.split("").reverse().join("")
// };

// console.log(getReverse("hello"));
// console.log(getReverse("devex"));


// yechim: 2
// loop orqali reverse qilish
// function getReverse2(word) {
//     let reverseWord = "";
//     for (let i = word.length - 1; i >= 0; i--) {
//         reverseWord += word[i]
//     }
//     return reverseWord
// };

// const result = getReverse2("Good morning");
// console.log(result)