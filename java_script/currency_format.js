/*
How to format a number as a US currency string in JavaScript
https://youtu.be/93wEPHMdQCI
*/
const formatter = new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'});
const our_number = 575.98;
const money_format = formatter.format(our_number);
console.log(money_format);
