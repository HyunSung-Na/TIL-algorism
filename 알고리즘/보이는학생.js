const seeT = cm => {
    let number = 0;
    let max = 0;

    cm.forEach((element, index, arr) => {
        if (arr[index] > max) {
            number += 1;
            max = arr[index];
        }        
    });

    return number;
}

const cm = [130, 135, 148, 140, 145, 150, 150, 153];

console.log(seeT(cm));