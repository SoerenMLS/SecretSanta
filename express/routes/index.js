var path = require('path');
var express = require('express');
var router = express.Router();

let nisseArray = ['Lasse', 'Bef', 'Albert', 'MB', 'Dencklez', 'Yung', 'Phil', 'Adrian'];
let antiNisseArray = [];

/* GET home page. */
router.get('/', function(req, res, next) {
  res.sendFile(path.join(__dirname + '/../index.html'));
});

module.exports = router;
