/**
 * Created by iury on 3/8/15.
 */
angular.module('FastFindApp').directive('productList', function(){
    return {
        restrict: 'E',
        replace: true,
        templateUrl: '/static/components/product/productList.html',
        scope: {
            products: "="
        },
        controller: function($scope, ProductModel){
            var pm = $scope.pm = ProductModel;
        }
    }
});
