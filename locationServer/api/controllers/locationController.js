'use strict';

var mongoose = require('mongoose'),
  LatLngDb = mongoose.model('LatLng');

exports.hello = function(req, res) {
    res.send("Please work");
};
exports.get_all = function(req, res) {
   LatLngDb.find({}).then(eachOne =>{
    res.json(eachOne);
    console.log(eachOne.lat)
   })
};

exports.get_random = function(req, res) {
  LatLngDb.count().exec(function(err, count){

    var random = Math.floor(Math.random() * count);

    LatLngDb.findOne().skip(random).exec(
      function (err, result) {
        if(err)
          res.send(err)
        res.json(result)
        // result is random 

    });

  });
};

exports.push_a_location = function(req, res) {
  console.log(req)
  var new_location = new LatLngDb(
    {
      lat: req.body.lat,
      lon: req.body.lon,
      country: req.body.country

    }
    );
  console.log(req)
  new_location.save(function(err, e) {
    if (err)
      res.send(err);
    res.json(e);
  });
};

exports.delete_all = function(req, res) {
  LatLngDb.remove({}, function(err){
        if(err){
          res.send(err)
        }
        else{
          res.end('success')
        }

      } 

    )
};
