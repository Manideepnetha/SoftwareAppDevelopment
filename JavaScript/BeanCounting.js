const str = "Software App Development"
const string = "Assignment 12 Java Script"
const letter = 't'

function CountBC(str1) {
    count = 0;
    for(let i = 0; i < str.length; i++){
        if(str[i] === "p"){
            count++;
        }
    }
    console.log(count)
    }
CountBC(str)


function CountChar(string,letter){
    count = 0;
    for(let i = 0; i<string.length;i++){
        if(string[i] === letter){
            count++;
        }
    }
    console.log(count)
}
CountChar(string,letter)