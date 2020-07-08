function find_next_greater_number(num) {

    // Creating Array of digits

    let split_num = [];
    while (num > 0) {
        split_num.push(num%10);
        num = Math.floor(num/10)
    }

    split_num = split_num.reverse();

    // Finding the digit which breaks the Descending order pattern from Right to left
    let i = split_num.length - 2;
    while (i >= 0) {
        if (split_num[i] < split_num[i + 1]){
            break;
        }
        i--;
    }

    // Check if all elements are in descending order - thus greater no. not possible
    if (i < 0) {
        return 'Not Possible';
    }

    // Find the next Greater single digit number
    let j = split_num.length - 1;
    while (j > i) {
        if (split_num[j] > split_num[i]){
            break;
        }
        j--;
    }

    // Swap breaking point with the smallest digit found which is bigger than the breaking point
    let temp = split_num[i];
    split_num[i] = split_num[j];
    split_num[j] = temp;

    // Splice and sort digits after the swaped digit and concat it again
    let part = split_num.splice(i+1, split_num.length  - i -  1)

    split_num = split_num.concat(part.sort());

    // Generate the new number
    let next_greater_number = 0

    i = 0
    while (i < split_num.length) {
        next_greater_number = next_greater_number * 10 + split_num[i];
        i++;
    }


    return next_greater_number;

}


let num = 3281;
console.log(num, find_next_greater_number(num));


num = 576;
console.log(num, find_next_greater_number(num));

num = 12345;
console.log(num, find_next_greater_number(num));

num = 9876;
console.log(num, find_next_greater_number(num));

num = 14873;
console.log(num, find_next_greater_number(num));

num = 17843;
console.log(num, find_next_greater_number(num));