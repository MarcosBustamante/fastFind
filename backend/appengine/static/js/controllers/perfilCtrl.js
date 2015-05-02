/**
 * Created by bustamante on 5/1/15.
 */

angular.module('FastFindApp').controller('PerfilCtrl', function(Ajax, $scope){
    $scope.user = window.FF.user;

    $scope.save = function(){
        Ajax.post('perfil/home/save', $scope.user).error(function(error){
            console.error('deu merda');
        });
    }
});
