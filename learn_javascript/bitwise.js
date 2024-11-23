let num1 = 5;  // In binary, 5 is 0101
let num2 = 3;  // In binary, 3 is 0011
let andResult = num1 & num2;  // 0101 & 0011 => 0001, so andResult is 1
console.log("AND Result:", andResult);  // Expected output: 1
let orResult = num1 | num2;   // 0101 | 0011 => 0111, so orResult is 7
console.log("OR Result:", orResult);  // Expected output: 7
let xorResult = num1 ^ num2;  // 0101 ^ 0011 => 0110, so xorResult is 6
console.log("XOR Result:", xorResult);  // Expected output: 6
let notResult = ~num1;  // ~0101 => 1010 (in two's complement form, this results in -6)
console.log("NOT Result:", notResult);  // Expected output: -6
let leftShiftResult = num1 << 1;  // 0101 << 1 => 1010, so leftShiftResult is 10
console.log("Left Shift Result:", leftShiftResult);  // Expected output: 10
let rightShiftResult = num1 >> 1;  // 0101 >> 1 => 0010, so rightShiftResult is 2
console.log("Right Shift Result:", rightShiftResult);  // Expected output: 2
let zeroFillShiftResult = num1 >>> 1;  // 0101 >>> 1 => 0010, same as >> for positive numbers
console.log("Zero-fill Right Shift Result:", zeroFillShiftResult);  // Expected output: 2
