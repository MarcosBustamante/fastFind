/**
 * Created by iury on 3/8/15.
 */
angular.module('FastFindApp').controller('HomeCtrl', function($scope, ProductModel){
    var pm = $scope.pm = ProductModel;
    $scope.products = pm.find('xbox');
    $scope.showForum = false;
    $scope.interval = 4000;
    $scope.showInformation = true;
    $scope.toggleForum = function(){
        $scope.showForum = !$scope.showForum;
    };

    $scope.toggleStore = function(){
        $scope.showInformation = !$scope.showInformation;
    };
});
