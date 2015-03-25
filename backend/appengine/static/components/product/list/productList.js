/**
 * Created by bustamante on 3/8/15.
 */
angular.module('FastFindApp').directive('productList', function(){
    return {
        restrict: 'E',
        replace: true,
        templateUrl: '/static/components/product/list/productList.html',
        scope: {
            products: "="
        },
        controller: function($scope, ProductModel){
            var pm = $scope.pm = ProductModel;
        }
    }
});
