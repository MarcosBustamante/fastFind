/**
 * Created by bustamante on 3/9/15.
 */
angular.module('FastFindApp').directive('store', function(){
    return {
        restrict: 'E',
        replace: true,
        templateUrl: '/static/components/store/store.html',
        scope: {
            productSelected: "="
        }
    }
});
