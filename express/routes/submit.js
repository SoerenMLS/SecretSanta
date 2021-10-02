var express = require('express');
var router = express.Router();

let nisseArray = ['Lasse', 'Bef', 'Albert', 'MB', 'Dencklez', 'Yung', 'Phil', 'Adrian'];
let antiNisseArray = [];

router.post('/', (req, res) =>{
    const name = req.body.name;
    let roll;
  
    do{
      roll = (Math.floor(Math.random() * 100)) % nisseArray.length;
    } while(nisseArray[roll] === name);

    nisseObj = { name: nisseArray[roll]}
  
    console.log(name + ' is the secret santa of ' + nisseArray[roll]);
    console.log(nisseArray + ' Is in the current array before splice ');
    console.log('The entry of ' + nisseArray[roll] + ' has been removed from nisseArray and been added to the antiNisseArray: ')
    antiNisseArray.push(nisseArray.splice(roll, 1));
    console.log(antiNisseArray)
    console.log('The remaining people that needs a secret santa are: ' + nisseArray)
    res.send(nisseObj);

  });

  module.exports = router;