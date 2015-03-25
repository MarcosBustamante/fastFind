/**
 * Created by bustamante on 3/5/15.
 */
angular.module('FastFindApp').directive('fastNavbar', function(){
    return {
        restrict: 'E',
        replace: true,
        templateUrl: '/static/components/navbar/navbar.html',
        scope: {},
        controller: function($scope, SidebarModel){
            var sbm = $scope.sbm = SidebarModel;
        }
    }
});
