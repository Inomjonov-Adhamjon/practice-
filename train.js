// TASK E

// Shunday function tuzing, u bitta string argumentni 
// qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"


// yechim:
// split("") stringni arrayga individual charachterlarga ajratadi
// reverse() ajratilgan value ni teskari qiladi 
// join("") esa teskari qilingan individual stringlarni 
// qaytadan bir string ga birlashtiradi.

function getReverse(a) {
    return a.split("").reverse().join("")
};

console.log(getReverse("hello"));
console.log(getReverse("devex"));


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