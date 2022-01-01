const my_array = [3,4,5,6];
console.log(my_array);
const id = my_array.indexOf(4);
if(id > -1){
   my_array.splice(id,1);
}
console.log(my_array);
