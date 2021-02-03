'use strict';
var mongoose = require('mongoose');
var Schema = mongoose.Schema;


// var LocationSchema = new Schema({
//   lat: {
//     type: String,
//     required: 'Enter Latitude'
//   },
//   lon: {
//     type: Number,
//     required: 'Enter Longitude'
//   },
//   Created_date: {
//     type: Date,
//     default: Date.now
//   },
// });
const LocationSchema = new Schema({
   lat: Number,
   lon: Number
});

module.exports = mongoose.model('LatLng', LocationSchema);

// C:\Program Files\MongoDB\Server\4.4\bin>mongod.exe -dbpath "C:\data"
// C:\Program Files\MongoDB\Server\4.4\bin>mongo.exe