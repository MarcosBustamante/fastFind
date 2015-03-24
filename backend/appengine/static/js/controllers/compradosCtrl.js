/**
 * Created by iury on 3/23/15.
 */
angular.module('FastFindApp').controller('CompradosCtrl', function($scope, ProductModel){
    var pm = $scope.pm = ProductModel;
    $scope.products = pm.find('xbox');
});
