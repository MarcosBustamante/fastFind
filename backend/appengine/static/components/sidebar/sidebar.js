/**
 * Created by bustamante on 3/6/15.
 */
angular.module('FastFindApp').factory('SidebarModel', function(){
    var status = true;

    var toggleSidebar = function(){
        status = !status;
    };

    var isOpen = function(){
        return status;
    };

    return {
        toggleSidebar: toggleSidebar,
        isOpen: isOpen
    }
});

angular.module('FastFindApp').directive('fastSidebar', function(){
    return {
        restrict: 'E',
        templateUrl: '/static/components/sidebar/sidebar.html',
        scope: {},
        controller: function($scope, SidebarModel){
            var sbm = $scope.sbm = SidebarModel;
            $scope.FF = window.FF;

            $scope.icons = [
                {
                    img: 'glyphicon-home',
                    label: 'Home',
                    link: '/home'
                },
                {
                    img: 'glyphicon-heart',
                    label: 'Lista de Desejos',
                    link: '/desejos'
                },
                {
                    img: 'glyphicon-star',
                    label: 'Lista de Compra',
                    link: '/comprados'
                },
                //{
                //    img: 'glyphicon-question-sign',
                //    label: 'Quem somos',
                //    link: '/historia'
                //}
            ]
        }
    }
});
