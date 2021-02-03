'use strict';


var mongoose = require('mongoose'),
  LatLngDb = mongoose.model('LatLng');

exports.get_random_location = function(req, res) {
  // LatLngDb.findById(0, function(err, task) {
  //   if (err)
  //     res.send(err);
  //   res.json(task);
  // });
  // LatLngDb.find({}, function(err, task) {
  //   if (err)
  //     res.send(err);
  //   console.log(task)
  //   res.json(task);
  // });
   LatLngDb.find({}).then(eachOne =>{
    res.json(eachOne);
    console.log(eachOne.lat)
   })
};

exports.push_a_location = function(req, res) {
  var new_location = new LatLngDb(
    {
      lat: req.params.lat,
      lon: req.params.lon

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
  LatLngDb.find({}).then(eachOne =>{
    remove(eachOne)
    res.json(eachOne);
    console.log(eachOne.lat)
   })
};