/**
 * Created by iury on 3/8/15.
 */
angular.module('FastFindApp').directive('productBlock', function(){
    return {
        restrict: 'E',
        replace: true,
        templateUrl: '/static/components/product/block/productBlock.html',
        scope: {
            products: "=",
            title: "@"
        },
        controller: function($scope, ProductModel){
            var pm = $scope.pm = ProductModel;
        }
    }
});
