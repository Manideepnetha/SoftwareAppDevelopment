function DeepEqual(D, E) {
    if (D === E) {
      return true;

    } else if (typeof D === 'object' && D !== null && typeof E === 'object' && E !== null) {
     
      let keys = Object.keys(D).concat(Object.keys(E));
      for (i of keys) {
        if (typeof D[i] === 'object' && typeof E[i] === 'object') {
          if (DeepEqual(D[i], E[i]) === false) {
            return false;
          }
        }
        
        else if (D[i] !== E[i]) {
          return false;
        }
      }
      return true;

    } else {
     return false; 
    }
  }

obj1 = {fn:"Admission",ls:"GAT"}
obj2 = {fn:"Admission",ls:"GAT"}

obj3 = {fn:"Msit",ls:"Placements"}
obj4 = {fn:"Placed",ls:"Students"}

str1 = "Course"
str3 = "Viva"
str2 = 300

console.log(DeepEqual(obj1,obj2))
console.log(DeepEqual(obj3,obj4))
console.log(DeepEqual(str1,str2))
console.log(DeepEqual(str2,str2))