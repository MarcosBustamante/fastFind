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
                    link: '/home',
                    is_visible: true
                },
                {
                    img: 'glyphicon-heart',
                    label: 'Produtos Desejados',
                    link: '/produtos/desejados'
                },
                {
                    img: 'glyphicon-star',
                    label: 'Produtos Comprados',
                    link: '/produtos/comprados'
                },
                {
                    img: 'glyphicon-barcode',
                    label: 'Cadastrar produtos',
                    link: '/cadastro/produtos'
                },
                {
                    img: 'glyphicon-briefcase',
                    label: 'Cadastrar Loja',
                    link: '/cadastro/lojas'
                }
            ]
        }
    }
});
