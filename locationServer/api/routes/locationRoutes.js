'use strict';
module.exports = function(app) {
  var locationController = require('../controllers/locationController');
	app.route('/')
		.get(locationController.hello)
	app.route('/getAll')
		.get(locationController.get_all)
	app.route('/getRandom')
		.get(locationController.get_random)
	app.route('/putLocation')
		.post(locationController.push_a_location)
	app.route('/deleteAll')
		.put(locationController.delete_all)
};