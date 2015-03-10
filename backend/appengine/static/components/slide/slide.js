/**
 * Created by iury on 3/9/15.
 */
angular.module('FastFindApp').directive('fastSlide', function(){
    return {
        restrict: 'E',
        replace: true,
        transclude: true,
        templateUrl: '/static/components/slide/slide.html',
        scope: {
            images: '=',
            interval: '=',
            title: '@?'
        }
    }
});
