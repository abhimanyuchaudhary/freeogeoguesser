'use strict';
module.exports = function(app) {
  var locationController = require('../controllers/locationController');

  app.route('/getAll')
    .get(locationController.get_all)
    app.route('/getRandom')
      .get(locationController.get_random)
    app.route('/putLocation/:lat/:lon/:country')
    .post(locationController.push_a_location)
     app.route('/deleteAll')
    .put(locationController.delete_all)
};