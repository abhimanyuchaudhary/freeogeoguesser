'use strict';
module.exports = function(app) {
  var locationController = require('../controllers/locationController');

  app.route('/getRandom')
    .get(locationController.get_random_location)

    app.route('/putLocation/:lat/:lon')
    .post(locationController.push_a_location)
     app.route('/deleteAll')
    .put(locationController.delete_all)
};